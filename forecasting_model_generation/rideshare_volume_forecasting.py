import pandas as pd
from sodapy import Socrata
from fbprophet import Prophet

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

# Change column names to fit Prophet module format requirements
historical_data.columns = ['ds', 'y']

# Instantiate and fit Facebook Prophet model
my_model = Prophet()

# Add holiday regressors
my_model.add_country_holidays(country_name='US')

# Fit and Predict
my_model.fit(historical_data)

future_dates = my_model.make_future_dataframe(periods=168, freq='1h')

forecast = my_model.predict(future_dates)

forecast = forecast[['ds', 'yhat']]

# Set negative values to 0
forecast.yhat = forecast.yhat.apply(lambda x: 0 if x < 0 else x)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set axis size
    fig, ax = plt.subplots(figsize=(30, 10))

    # Plot Forecast
    sns.lineplot(y='yhat', x='ds', data=forecast)