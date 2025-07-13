from datetime import datetime, timedelta

def full_items():
## add more data to this list
    items = [
    {"name": "Paracetamol", "company": "Cipla", "expiry": "2026-03-01", "total_purchase": 500, "last_restock_date": "2024-04-01", "sell": 300},
    {"name": "Dolo 650", "company": "Micro Labs", "expiry": "2025-12-01", "total_purchase": 800, "last_restock_date": "2024-06-15", "sell": 700},
    {"name": "Maggiee", "company": "Nestle", "expiry": "2025-08-11", "total_purchase": 800, "last_restock_date": "2024-05-10", "sell": 750},
    {"name": "Cetrizine", "company": "Sun Pharma", "expiry": "2024-08-03", "total_purchase": 1000, "last_restock_date": "2024-01-10", "sell": 1000},
    {"name": "iPhone 13", "company": "Apple", "expiry": "2030-12-31", "total_purchase": 100, "last_restock_date": "2025-01-05", "sell": 95},
    {"name": "Toothpaste", "company": "Colgate", "expiry": "2025-11-01", "total_purchase": 1200, "last_restock_date": "2024-03-10", "sell": 1000},
    {"name": "Shampoo", "company": "Head & Shoulders", "expiry": "2025-06-01", "total_purchase": 600, "last_restock_date": "2024-04-22", "sell": 550},
    {"name": "Bread", "company": "Wonder", "expiry": "2024-07-15", "total_purchase": 300, "last_restock_date": "2024-07-01", "sell": 280},
    {"name": "Milk", "company": "DairyPure", "expiry": "2024-07-13", "total_purchase": 500, "last_restock_date": "2024-07-10", "sell": 470},
    {"name": "Eggs", "company": "Eggland", "expiry": "2024-07-20", "total_purchase": 400, "last_restock_date": "2024-07-08", "sell": 390},
    {"name": "Pain Relief Balm", "company": "Vicks", "expiry": "2026-01-01", "total_purchase": 300, "last_restock_date": "2024-06-01", "sell": 290},
    {"name": "Face Wash", "company": "Clean & Clear", "expiry": "2025-10-10", "total_purchase": 500, "last_restock_date": "2024-04-17", "sell": 460},
    {"name": "Coca-Cola", "company": "Coca-Cola", "expiry": "2025-01-15", "total_purchase": 1000, "last_restock_date": "2024-06-10", "sell": 950},
    {"name": "Pepsi", "company": "PepsiCo", "expiry": "2024-12-15", "total_purchase": 800, "last_restock_date": "2024-05-25", "sell": 780},
    {"name": "Hand Sanitizer", "company": "Dettol", "expiry": "2025-06-30", "total_purchase": 700, "last_restock_date": "2024-02-01", "sell": 680},
    {"name": "Disinfectant", "company": "Lysol", "expiry": "2026-03-01", "total_purchase": 450, "last_restock_date": "2024-06-20", "sell": 430},
    {"name": "Laptop", "company": "HP", "expiry": "2030-01-01", "total_purchase": 50, "last_restock_date": "2025-05-05", "sell": 48},
    {"name": "Coffee", "company": "Nescafe", "expiry": "2026-01-15", "total_purchase": 900, "last_restock_date": "2024-04-05", "sell": 850},
    {"name": "Tea", "company": "Tata Tea", "expiry": "2026-02-01", "total_purchase": 850, "last_restock_date": "2024-03-01", "sell": 820},
    {"name": "Biscuits", "company": "Oreo", "expiry": "2025-10-05", "total_purchase": 750, "last_restock_date": "2024-04-11", "sell": 700},
    {"name": "Energy Drink", "company": "Red Bull", "expiry": "2025-12-12", "total_purchase": 600, "last_restock_date": "2024-06-01", "sell": 580},
    {"name": "Soap", "company": "Dove", "expiry": "2026-08-15", "total_purchase": 800, "last_restock_date": "2024-04-22", "sell": 760},
    {"name": "Toilet Paper", "company": "Charmin", "expiry": "2030-01-01", "total_purchase": 1000, "last_restock_date": "2024-05-20", "sell": 980},
    {"name": "Detergent", "company": "Tide", "expiry": "2027-01-01", "total_purchase": 700, "last_restock_date": "2024-03-15", "sell": 670},
    {"name": "Bleach", "company": "Clorox", "expiry": "2026-09-01", "total_purchase": 400, "last_restock_date": "2024-06-25", "sell": 380},
    {"name": "Smartwatch", "company": "Samsung", "expiry": "2030-12-31", "total_purchase": 100, "last_restock_date": "2025-06-10", "sell": 97},
    {"name": "Smart TV", "company": "LG", "expiry": "2030-12-31", "total_purchase": 60, "last_restock_date": "2025-05-20", "sell": 55},
    {"name": "Chips", "company": "Lays", "expiry": "2025-08-01", "total_purchase": 1000, "last_restock_date": "2024-06-15", "sell": 950},
    {"name": "Juice", "company": "Tropicana", "expiry": "2024-11-30", "total_purchase": 700, "last_restock_date": "2024-06-01", "sell": 680},
    {"name": "Chocolate", "company": "Cadbury", "expiry": "2025-04-01", "total_purchase": 800, "last_restock_date": "2024-03-10", "sell": 790},
    {"name": "Sanitary Pads", "company": "Whisper", "expiry": "2026-02-01", "total_purchase": 500, "last_restock_date": "2024-06-20", "sell": 470},
    {"name": "Baby Diapers", "company": "Pampers", "expiry": "2026-01-01", "total_purchase": 650, "last_restock_date": "2024-05-01", "sell": 630},
    {"name": "Face Mask", "company": "3M", "expiry": "2026-10-10", "total_purchase": 400, "last_restock_date": "2024-02-10", "sell": 390},
    {"name": "Printer", "company": "Canon", "expiry": "2030-01-01", "total_purchase": 80, "last_restock_date": "2025-03-01", "sell": 75},
    {"name": "Keyboard", "company": "Logitech", "expiry": "2030-01-01", "total_purchase": 150, "last_restock_date": "2025-04-05", "sell": 145},
    {"name": "Mouse", "company": "Logitech", "expiry": "2030-01-01", "total_purchase": 150, "last_restock_date": "2025-04-05", "sell": 140},
    {"name": "Cooking Oil", "company": "Fortune", "expiry": "2025-12-01", "total_purchase": 900, "last_restock_date": "2024-03-10", "sell": 850},
    {"name": "Rice", "company": "India Gate", "expiry": "2026-05-01", "total_purchase": 1000, "last_restock_date": "2024-06-15", "sell": 970},
    {"name": "Flour", "company": "Pillsbury", "expiry": "2025-09-01", "total_purchase": 800, "last_restock_date": "2024-05-10", "sell": 770},
    {"name": "Salt", "company": "Tata", "expiry": "2027-01-01", "total_purchase": 1100, "last_restock_date": "2024-04-01", "sell": 1050},
    {"name": "Sugar", "company": "Dhampure", "expiry": "2026-06-01", "total_purchase": 1000, "last_restock_date": "2024-04-10", "sell": 950},
    {"name": "Ketchup", "company": "Heinz", "expiry": "2025-10-01", "total_purchase": 600, "last_restock_date": "2024-05-15", "sell": 580},
    {"name": "Hair Oil", "company": "Parachute", "expiry": "2025-11-01", "total_purchase": 700, "last_restock_date": "2024-06-01", "sell": 690},
    {"name": "Perfume", "company": "AXE", "expiry": "2027-12-01", "total_purchase": 300, "last_restock_date": "2024-02-20", "sell": 280},
    {"name": "Notebook", "company": "Classmate", "expiry": "2030-01-01", "total_purchase": 900, "last_restock_date": "2024-06-10", "sell": 870},
    {"name": "Pen", "company": "Reynolds", "expiry": "2030-01-01", "total_purchase": 1000, "last_restock_date": "2024-06-05", "sell": 990},
    {"name": "Battery", "company": "Duracell", "expiry": "2029-01-01", "total_purchase": 500, "last_restock_date": "2024-03-20", "sell": 480},
    {"name": "Toaster", "company": "Philips", "expiry": "2030-01-01", "total_purchase": 60, "last_restock_date": "2025-04-15", "sell": 58},
    {"name": "Play Station", "company": "Sony", "expiry": "None", "total_purchase": 10, "last_restock_date": "2025-04-15", "sell": 5}
]
    return items

from datetime import datetime, timedelta

def get_items():
    items = full_items()
    today = datetime.today()
    filtered_items = []

    for item in items:
        # Handle expiry date safely
        if item['expiry'] in (None, "None", ""):
            expiry_date = None
        else:
            expiry_date = datetime.strptime(item['expiry'], "%Y-%m-%d")

        # Calculate remaining stock
        remaining = item['total_purchase'] - item['sell']
        if remaining <= 0:
            continue  # Skip items with no stock

        # Calculate efficiency
        efficiency = item['sell'] / item['total_purchase']

        # Expiring within 30 days?
        expiring_soon = False
        if expiry_date:
            expiring_soon = expiry_date <= (today + timedelta(days=30))

        # Set a value for sorting even if expiry_date is None
        expiry_sort_value = expiry_date if expiry_date else datetime.max

        # Enrich the item
        item['efficiency'] = efficiency
        item['remaining'] = remaining
        item['expiring_soon'] = expiring_soon
        item['expiry_sort'] = expiry_sort_value

        filtered_items.append(item)

    # Optional: sort by expiry (soonest first)
    filtered_items.sort(key=lambda x: x['expiry_sort'])

    return filtered_items