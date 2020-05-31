# rideshare_volume_forecasting_with_flask
A web app which showcases forecasted rideshare volume in Chicago built on Flask

# TO DO
- Add to html page using web app framework (Need to research web app frameworks like bootstrap)
- Define AWS and web architecture to host application. Save historical data in S3, use Lambda function to run forecasting models and save back in S3, have web app query S3 for visuals

# Done
- Update function documentation 
- Add functionality to have a html radio button form which allows users to switch between visuals of forecasts made with Prophet, TBATS, and SARIMA
- Show past 2 weeks of historical data on same line chart as forecasts, with historical in blue and forecasts in orange 
