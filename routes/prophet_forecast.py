# from app import app
#
# from flask import Flask, render_template,request
# import plotly
# import plotly.graph_objs as go
#
# import pandas as pd
# import numpy as np
# import json
#
# prophet_forecast = pd.read_csv(r'..\rideshare_webapp\data\prophet_forecast.csv')
#
# @app.route('/')
# def index():
#     line = create_plot(prophet_forecast)
#     return render_template('forecast_view.html', plot=line)
#
# def create_plot(prophet_forecast):
#
#     data = [
#         go.Scatter(
#             x=prophet_forecast['ds'],
#             y=prophet_forecast['yhat']
#         )
#     ]
#
#     layout = go.Layout(margin=dict(pad=5), xaxis_title="Date",yaxis_title="Number of Rides")
#
#     fig = go.Figure(data=data,layout=layout)
#
#     graphJSON = fig.to_json()
#
#     return graphJSON