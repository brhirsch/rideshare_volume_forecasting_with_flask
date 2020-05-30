import pandas as pd
from sodapy import Socrata
from forecasting_functions import *

application_id = 'WvpiRPNr9Eq21W0kctAqodZYj'

# Query Chicago City API
client = Socrata("data.cityofchicago.org", application_id)

historical_data = client.get("wrvz-psew", where='trip_start_timestamp > \'2020-03-20T00:00:00.000\'', limit=100000000)

# Convert to pandas DataFrame
historical_data = pd.DataFrame.from_records(historical_data)

# Count rides, select specific columns, clean date column, group by hour
historical_data['counter'] = 1

historical_data = historical_data[['company', 'fare', 'trip_start_timestamp', 'counter']]

historical_data.trip_start_timestamp = pd.to_datetime(historical_data.trip_start_timestamp)
historical_data.trip_start_timestamp = historical_data.trip_start_timestamp.dt.strftime('%Y-%m-%d %H')
historical_data.trip_start_timestamp = pd.to_datetime(historical_data.trip_start_timestamp)

historical_data = pd.DataFrame(historical_data.groupby('trip_start_timestamp')['counter'].sum())

historical_data = historical_data.reset_index().sort_values(by='trip_start_timestamp')

historical_data = historical_data[['trip_start_timestamp', 'counter']]

prophet_forecast = make_prophet_forecast(historical_data)

# Create csv file of 2 week forecast using prophet and save in app directory
prophet_forecast.to_csv(r'../app/prophet_forecast.csv')

# Create csv file for historical data
historical_data.to_csv(r'../app/historical_data.csv')
