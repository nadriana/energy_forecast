from prophet import Prophet

class ProphetService:
    "This is a prophet service class"

    def __init__(self, df=''):
        self.df = df
    

    def forecast(self):
        m = Prophet()
        m.fit(self.df)
        
        future = m.make_future_dataframe(freq = "H", periods = 24)
        forecast = m.predict(future)
        prophet_fcst = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(24)
        return prophet_fcst
