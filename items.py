def get_items():
## add more data to this list
    items = [
        {
            "name": "Paracetamol",
            "company": "Cipla",
            "expiry": "2026-03-01",
            "total_purchase": 500,
            "sell": 300
        },
        {
            "name": "Dolo 650",
            "company": "Micro Labs",
            "expiry": "2025-12-01",
            "total_purchase": 800,
            "sell": 700
        },
        {
            "name": "Maggiee",
            "company": "Nestle",
            "expiry": "2025-08-11",
            "total_purchase": 800,
            "sell": 750
        }
    ]

    for item in items:
        item['efficiency'] = (item['total_purchase'] - item['sell']) / item['total_purchase']

    return items
