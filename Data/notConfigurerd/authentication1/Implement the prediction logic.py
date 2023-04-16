from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from bson import json_util
from django.http import JsonResponse
from PredictionModel.models import Stocks


def predict_stock_price(request):
    symbol = request.GET.get('symbol', 'AAPL')
    days = int(request.GET.get('days', 30))

    # Retrieve historical stock prices from MongoDB
    prices = Stocks.find({'symbol': symbol, 'date': {'$gte': datetime.now() - timedelta(days=days)}})
    X = []
    y = []
    for price in prices:
        X.append([(price['date'] - datetime(1970, 1, 1)).total_seconds()])
        y.append(price['price'])

    # Fit a linear regression model to the data
    model = LinearRegression()
    model.fit(X, y)

    # Predict future stock prices
    future_dates = [datetime.now() + timedelta(days=i) for i in range(1, days + 1)]
    future_X = [[(date - datetime(1970, 1, 1)).total_seconds()] for date in future_dates]
    future_prices = model.predict(future_X)

    # Return the predicted prices as a JSON response
    data = [{'date': date.strftime('%Y-%m-%d'), 'price': price} for date, price in zip(future_dates, future_prices)]
    return JsonResponse(json_util.dumps(data), safe=False)




# This view retrieves historical stock prices from the MongoDB database for a given symbol and number of days, 
# fits a linear regression model to the data, and predicts future stock prices for the next days days.

