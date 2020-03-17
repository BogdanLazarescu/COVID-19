import json
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta

datetimeFormat = '%Y-%m-%d'
today= '2020-03-17'  #specify todays date

#param min_cases - only show data from the date when a number of 'min cases' were registered
def plot_country(data, countries, min_cases=20):
    color = 0
    for country in countries:
        for p in data[country]:
            print('Date: ' + p['date'])
            print('Confirmed: ' + str(p['confirmed']))
            print('Deaths: ' + str(p['deaths']))
            print('Recovered: ' + str(p['recovered']))
            print('')
            if p['confirmed'] >= min_cases:
                days_diff = datetime.datetime.strptime(p['date'], datetimeFormat) \
                       - datetime.datetime.strptime(today, datetimeFormat)

                date = p['date'][p['date'].index('-')+1:]
                cases= p['confirmed']
                plt.plot(days_diff.days, cases, 'C'+str(color)+'o')
        color+=1
        plt.legend

    plt.legend()
    plt.show()


with open('timeseries.json') as json_file:
    data = json.load(json_file)

plot_country(data, ["Romania","United Kingdom", "Japan", "Italy"], min_cases=20)