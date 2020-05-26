from fbprophet import Prophet


def make_prophet_forecast(historical_data, periods=168, freq='1h'):

    # Change column names to fit Prophet module format requirements
    historical_data.columns = ['ds', 'y']

    # Instantiate and fit Facebook Prophet model
    my_model = Prophet()

    # Add holiday regressors
    my_model.add_country_holidays(country_name='US')

    # Fit and Predict
    my_model.fit(historical_data)

    future_dates = my_model.make_future_dataframe(periods=periods, freq=freq)

    forecast = my_model.predict(future_dates)

    forecast = forecast[['ds', 'yhat']]

    # Set negative values to 0
    forecast.yhat = forecast.yhat.apply(lambda x: 0 if x < 0 else x)

    return forecast
