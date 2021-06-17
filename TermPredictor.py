
# Data Source
import yfinance as yf
# Data viz
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime


class TermPredictor:

    def __init__(self, operation):
        self.operation = operation;
        self.app = dash.Dash(__name__)
        self.app.layout = self.serve_layout
        # Show
        self.app.run_server()
        

    def serve_layout(self):
        colors = {
            'background': '#111111',
            'text': '#7FDBFF'
        }
        now = datetime.datetime.now()
        # Importing market data
        data = yf.download(tickers=self.operation, period='8d', interval="60m")

        # Adding Moving average calculated field
        data['MA5'] = data['Close'].rolling(5).mean()
        data['MA20'] = data['Close'].rolling(20).mean()
        # declare figure
        self.fig = go.Figure()

        # Candlestick
        self.fig.add_trace(go.Candlestick(x=data.index,
                                          open=data['Open'],
                                          high=data['High'],
                                          low=data['Low'],
                                          close=data['Close'], name='market data'))

        # Add Moving average on the graph
        self.fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(
            color='blue', width=1.5), name='Long Term MA'))
        self.fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(
            color='orange', width=1.5), name='Short Term MA'))

        # Updating X axis and graph
        # X-Axes
        self.fig.update_layout(
            title="Grafica: "+self.operation+" 60m",
            #plot_bgcolor=colors['background'],
            #paper_bgcolor=colors['background'],
            #font_color=colors['text']
        )
        self.fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=2, label="2d", step="day", stepmode="backward"),
                    dict(count=5, label="5d", step="day", stepmode="backward"),
                    dict(count=7, label="WTD", step="day", stepmode="todate"),
                    dict(step="all")
                ])
            )
        )
        # Importing market data
        data = yf.download(tickers=self.operation, period='8d', interval="90m")

        # Adding Moving average calculated field
        data['MA5'] = data['Close'].rolling(5).mean()
        data['MA20'] = data['Close'].rolling(20).mean()

        # declare figure
        self.fig2 = go.Figure()

        # Candlestick
        self.fig2.add_trace(go.Candlestick(x=data.index,
                                           open=data['Open'],
                                           high=data['High'],
                                           low=data['Low'],
                                           close=data['Close'], name='market data'))

        # Add Moving average on the graph
        self.fig2.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(
            color='blue', width=1.5), name='Long Term MA'))
        self.fig2.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(
            color='orange', width=1.5), name='Short Term MA'))

        # Updating X axis and graph
        # X-Axes
        self.fig2.update_layout(
            title="Grafica: "+self.operation+" 90m",
            #plot_bgcolor=colors['background'],
            #paper_bgcolor=colors['background'],
            #font_color=colors['text']
        )
        self.fig2.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=2, label="2d", step="day", stepmode="backward"),
                    dict(count=5, label="5d", step="day", stepmode="backward"),
                    dict(count=7, label="WTD", step="day", stepmode="todate"),
                    dict(step="all")
                ])
            )
        )
        return html.Div(children=[
            # All elements from the top of the page
            html.Div([
                dcc.Graph(id="graph", figure=self.fig),
            ]),
            # New Div for all elements in the new 'row' of the page
            html.Div([
                dcc.Graph(id="grapho", figure=self.fig2),
            ]),
        ])