import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from datetime import *
from ggplot import *

weather_turnstile = pd.read_csv('turnstile_weather_v2.csv')
total_riders_per_day=weather_turnstile.groupby(['DATEn'],as_index=False)['ENTRIESn_hourly'].sum()
list(total_riders_per_day.columns.values)
total_riders_per_day['DATEn'] = total_riders_per_day['DATEn'].apply(lambda x: datetime.strptime(x, "%m-%d-%y"))
total_riders_per_day.columns = ['date', 'total_entries']
print(total_riders_per_day[:3])
plot = ggplot(total_riders_per_day, aes(x='date', y='total_entries')) + geom_line() + stat_smooth(colour='blue', span=0.2) + theme(axis_text_x  = element_text(angle = 35, hjust = 1))
ggsave(plot, "riders_per_day.png")
    
