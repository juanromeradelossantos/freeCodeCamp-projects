import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (BMI > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].replace(1,0)
df['cholesterol'] = df['cholesterol'].replace([2,3],1)
df['gluc'] = df['gluc'].replace(1,0)
df['gluc'] = df['gluc'].replace([2,3],1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat_counts = df_cat.groupby(['cardio','variable'])['value'].value_counts()

    df_cat_counts.name = 'total'

    df_cat_counts = df_cat_counts.reset_index(['cardio','variable','value'])


    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat_counts, kind='bar')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    c1 = (df['ap_lo'] <= df['ap_hi'])
    c2 = (df['height'] >= df['height'].quantile(0.025))
    c3 = (df['height'] <= df['height'].quantile(0.975))
    c4 = (df['weight'] >= df['weight'].quantile(0.025))
    c5 = (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[c1 & c2 & c3 & c4 & c5]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape))

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, annot=True, mask=mask, linewidths=.5, fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
