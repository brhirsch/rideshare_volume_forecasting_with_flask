import plotly.graph_objs as go

def create_plot(data, chart_title, xaxis_title, yaxis_title):

    data = [
        go.Scatter(
            x=data['ds'],
            y=data['y']
        )
    ]

    layout = go.Layout(margin=dict(pad=5),title=chart_title, xaxis_title=xaxis_title,yaxis_title=yaxis_title)

    fig = go.Figure(data=data,layout=layout)

    graphJSON = fig.to_json()

    return graphJSON