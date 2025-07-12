from datetime import datetime, timedelta

def full_items():
## add more data to this list
    items = [
        {
            "name": "Paracetamol",
            "company": "Cipla",
            "expiry": "2026-03-01",
            "total_purchase": 500,
            "last_restock_date": "2024-04-01",
            "sell": 300
        },
        {
            "name": "Dolo 650",
            "company": "Micro Labs",
            "expiry": "2025-12-01",
            "total_purchase": 800,
            "last_restock_date": "2024-06-15",
            "sell": 700
        },
        {
            "name": "Maggiee",
            "company": "Nestle",
            "expiry": "2025-08-11",
            "total_purchase": 800,
            "last_restock_date": "2024-05-10",
            "sell": 750
        },
        {
            "name": "Cetrizine",
            "company": "Sun Pharma",
            "expiry": "2024-08-03",
            "total_purchase": 1000,
            "last_restock_date": "2024-01-10",
            "sell": 1000
        }
    ]
    return items
def get_items():
    items=full_items()
    today = datetime.today()
    filtered_items = []

    for item in items:
        expiry_date = datetime.strptime(item['expiry'], "%Y-%m-%d")
        remaining = item['total_purchase'] - item['sell']

        # Skip items with no stock
        if remaining <= 0:
            continue

        efficiency = remaining / item['total_purchase']
        expiring_soon = expiry_date <= (today + timedelta(days=30))

        item['efficiency'] = efficiency
        item['remaining'] = remaining
        item['expiring_soon'] = expiring_soon

        filtered_items.append(item)

    return filtered_items
