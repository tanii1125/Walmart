from datetime import datetime, timedelta
from items import get_items

def get_deals():
    today = datetime.today()
    cutoff = today + timedelta(days=30)

    items = get_items()

    # Filter items expiring within the next 30 days
    deals = [item for item in items if datetime.strptime(item['expiry'], "%Y-%m-%d") <= cutoff]

    return deals