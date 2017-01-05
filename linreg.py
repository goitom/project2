
import numpy as np
import pandas as pd
import statsmodels.api as sm

'''
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.
'''

'''Read in the .csv file'''

weather_turnstile = pd.read_csv('turnstile_weather_v2.csv')
weather_turnstile['wkday_hour_intrcn'] = weather_turnstile['weekday']*weather_turnstile['hour']
weather_turnstile['wkday_fog_intrcn'] = weather_turnstile['weekday']*weather_turnstile['fog']
def linear_regression(features, values):
	'''
	Perform linear regression given a data set with an arbitrary number of features.
	
	This can be the same code as in the lesson #3 exercise.
	'''
    
	features = sm.add_constant(features)
	model = sm.OLS(values,features)
	results = model.fit()
	intercept = results.params[0]
	params = results.params[1:]
	print(results.summary())
	return results, intercept, params

def predictions(dataframe):
	
	features = dataframe[['precipi', 'weekday', 'wkday_hour_intrcn', 'wkday_fog_intrcn','hour', 'meantempi', 'fog']]
	dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
	features = features.join(dummy_units)
    
    # Values
	values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
	results, intercept, params = linear_regression(features, values)
	
	predictions = intercept + np.dot(features, params)
	
predictions(weather_turnstile)