import numpy as np
import pandas as pd 
import yfinance as yf

tickers = ['AAPL', 'MSFT', 'SPY', 'QQQ', '^GSPC', '^FCHI', 'BTC-USD', 'ETH-USD', 'CL=F', 'GC=F']
# Téléchargement des données 
data = yf.download(tickers, start="2024-01-01", end="2024-10-31")
# Selection des prix à la clôture des séances journaliers
data_close = data["Close"]
data_close = data_close.dropna()
# Rendements journaliers
rend_jour = data_close.pct_change().dropna()
# Rendement annuel
rend_annuel = rend_jour.mean()*252
# Volatilité 
Vol = rend_jour.std()*(np.sqrt(252))
# VaR
VaR_95 = rend_jour.quantile(0.05)



# Résumé 


summary = pd.DataFrame({
    'Rendement annuel (%)' : rend_annuel*100,
    'Volatilité (%)': Vol*100,
    'VaR 95% journalière (%)': VaR_95*100 

}).round(2)




print(rend_jour) 


data_close.to_excel("prix.xlsx")

rend_jour.to_excel("rendements.xlsx")
 
summary.to_excel("Indicateurs_financiers_portefeuille.xlsx")
