import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize=(8,8))
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2050), intercept + slope*range(1880, 2050), color='r', linestyle='-', label='1st fit line')

    # Create second line of best fit
    slope2, intercept2, r_value, p_value, std_err = linregress(x=df[df['Year']>=2000]['Year'], y=df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2050), intercept2 + slope2*range(2000, 2050), color='b', linestyle='-', label='2nd fit line')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()