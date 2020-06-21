import numpy as np
import pandas as pd


# 1
photos_period = 5
bus_period = 8
number_of_days = 400

# 2
bus_stop = pd.DataFrame(index=range(number_of_days))

# 3
bus_stop['photos'] = bus_stop.index % photos_period == 0
bus_stop['schedule'] = bus_stop.index % bus_period == 0

# 4
bus_stop['representation'] = bus_stop['photos'] & bus_stop['schedule']

# 5
stop_count = bus_stop['schedule'].sum()
stop_rep_count = bus_stop['representation'].sum()
percentage = 100 * stop_rep_count / stop_count
print(f'There was {stop_count} stops.')
print(f'We caught {stop_rep_count} stops.')
print(f'We capture {percentage:.2f}% of the schedule.')

# 6
sampled_stops = bus_stop[bus_stop['representation']]
sampled_stops_periods = np.diff(sampled_stops.index)
print(f'The smallest time interval is {sampled_stops_periods.min()} days.')
