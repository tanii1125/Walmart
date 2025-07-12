from list import get_items

def get_predictions():
    predictions = []

    for item in get_items():
        remaining = item['total_purchase'] - item['sell']
        efficiency = item['efficiency']  # already calculated in list.py

        if remaining < 100:
            if efficiency < 0.3:
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

    return predictions
