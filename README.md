# urban_taxi_volume_forecasting_with_flask
A web app which visualizes historical and forecasted taxi ride volume in Chicago using an array of statistical forecasting models. 

The purpose of this project was to dive deeper into full stack development by incorporating the outputs of machine learning models into an application built in Python using the Flask framework, visualizations with Plotly, and a front end in html/bootstrap. 

![Network 1](https://github.com/brhirsch/urban_taxi_volume_forecasting_with_flask/blob/master/images/taxi_ride_volume_forecast.png)


# TO DO
- Rework CSS
- Define AWS and web architecture to host application
  1. Script to pull historical data, run models, save csv's to S3 
  2. Add code to pull csv's from S3 and use in Flask app on startup 
  3. Deploy Flask app on EC2

- Add rideshare volume forecasting for same date range in graph under taxi graph 

# Done
- Update function documentation 
- Add functionality to have a html form which allows users to switch between visuals of forecasts made with Prophet, TBATS, and SARIMA
- Show past 2 weeks of historical data on same line chart as forecasts
