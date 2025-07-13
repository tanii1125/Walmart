from datetime import datetime, timedelta
from items import get_items

def get_deals():
    today = datetime.today()
    cutoff = today + timedelta(days=30)

    items = get_items()
    deals = []

    for item in items:
        expiry_str = item.get('expiry')

        if expiry_str in (None, "None", ""):
            continue

        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d")

        if expiry_date <= cutoff:
            deals.append(item)

    return deals
