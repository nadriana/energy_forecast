import pandas as pd
import statsmodels.api as sm
from pandas.tseries.offsets import DateOffset

class ARIMAService:
    "This is an ARIMA service class"

    def __init__(self, df=''):
        self.df = df


    def forecast(self):
        self.df.drop(columns = ["Unnamed: 0"], inplace = True)
        self.df.sort_values(by = ["Datetime"], ascending = True, inplace = True)
        self.df.set_index("Datetime", inplace = True)

    
        ARIMA_model = sm.tsa.arima.ARIMA(self.df["Power_MWH"], order=(3,0,1))
        ARIMA_model = ARIMA_model.fit()

        prediction = pd.DataFrame(ARIMA_model.predict(len(self.df)+1, len(self.df)+24))   
        pred_date = [self.df.index[-1]+ DateOffset(hours = x) for x in range(1, 25)]
        pred_date = pd.DataFrame(index = pred_date, columns = self.df.columns)
        prediction.set_index(pred_date.index, inplace = True)
        prediction.rename(columns={"predicted_mean":"prediction"}, inplace = True)
        return prediction