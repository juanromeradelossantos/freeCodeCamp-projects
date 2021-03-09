def add_time(start, duration, day=None):
    week = ['Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_msg = ''
    week_day = ''
    days = 0
    
    minutes = int(start.split()[0].split(':')[1]) + int(duration.split(':')[1])
    hours = int(start.split()[0].split(':')[0]) + int(duration.split(':')[0])

    if start.split()[1] == 'PM':
      hours += 12

    if minutes >= 60:
        minutes -= 60
        hours += 1
    
    if hours >= 24:
        days = int(hours / 24)
        if days == 1:
             days_msg = '(next day)'
        elif days > 1:
             days_msg = '({} days later)'.format(days)
        hours %= 24
    
    if day:
        pos = week.index(day.capitalize())
        pos += days
        if pos > len(week)-1:
            pos %= len(week)
        week_day = week[pos]
    
    if hours == 12:
        period = 'PM'
    elif hours == 0:
        hours += 12
        period = 'AM'
    elif hours > 12:
        hours -= 12
        period = 'PM'
    else:
        period = 'AM'

    new_time = str(hours) + ':' + '{:0>2}'.format(str(minutes)) + ' ' + period
    if len(week_day) > 0:
        new_time += ', ' + week_day
    if len(days_msg) > 0:
        new_time += ' ' + days_msg


    return new_time
    