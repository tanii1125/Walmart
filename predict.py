from items import get_items,full_items
from datetime import datetime,timedelta
from trending import get_trending_items

def get_predictions():
    predictions = []

    for item in get_items():
        remaining = item['remaining']
        efficiency = item["efficiency"]*100
        #print(remaining,efficiency)
       
        if remaining < 100:
            if efficiency > 90:
                suggestion = "Buy More"
            else:
                suggestion = "Buy Less"
        else:
            suggestion = "Sufficient Stock"
        #print(suggestion)    
        predictions.append({
            "name": item["name"],
            "company": item["company"],
            "total_units":item["total_purchase"],
            "remaining": remaining,
            "efficiency": efficiency,
            "suggestion": suggestion
        })
        
#get_predictions()
    return predictions
def get_zero_stock_items():
    # Re-define full item list without filtering

    out_of_stock = []
    for item in full_items():
        remaining = item['total_purchase'] - item['sell']
        if remaining <= 0:
            out_of_stock.append({
                "name": item['name'],
                "company": item['company'],
                "sell": item['sell'],
                "total_purchase": item['total_purchase']
            })

    return out_of_stock

def get_restock_by_date_items():
    today = datetime.today()
    due_items = []

    for item in full_items():
        last_restock = datetime.strptime(item['last_restock_date'], "%Y-%m-%d")
        days_since_restock = (today - last_restock).days
        #predicted_date= demands, expiry, end of stock,festival
        if item['total_purchase']-item['sell']<30 or item['name'] in get_trending_items():
            predicted_date=today+timedelta(days=3)
        elif item['total_purchase']-item['sell']<50:
            predicted_date=today+timedelta(days=7)
        elif item['total_purchase']-item['sell']<100:
            predicted_date=today+timedelta(days=31)
        else:
            predicted_date=today+timedelta(days=50)
            
        if days_since_restock > 60:
            due_items.append({
                "name": item['name'],
                "company": item['company'],
                "last_restock_date": item['last_restock_date'],
                "days_since": days_since_restock,
                "predicted_date":predicted_date
            })

    return due_items
