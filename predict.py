from items import get_items,full_items
from datetime import datetime, timedelta

def get_predictions():
    predictions = []

    for item in get_items():
        remaining = item['total_purchase'] - item['sell']
        efficiency = item['efficiency']
        if efficiency <= 1:
            efficiency *= 100
        suggestion=""
        
        if remaining < 100:
            if efficiency > 70:
                suggestion = "Buy More"
            else:
                suggestion = "Buy Less"
        else:
            suggestion = "Sufficient Stock"
            
        predictions.append({
            "name": item['name'],
            "company": item['company'],
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

        if days_since_restock > 60:
            due_items.append({
                "name": item['name'],
                "company": item['company'],
                "last_restock_date": item['last_restock_date'],
                "days_since": days_since_restock
            })

    return due_items
