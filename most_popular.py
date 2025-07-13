from items import get_items

def get_most_popular_items():
    popular_items = []

    for item in get_items():
        sell = item['sell']
        total = item['total_purchase']
        efficiency =round(item['efficiency'], 2) # Higher is better

        popular_items.append({
            "name": item["name"],
            "company": item["company"],
            "sell": sell,
            "total": total,
            "efficiency": efficiency,
        })

    # Sort items by popularity score descending
    popular_items.sort(key=lambda x: x["efficiency"], reverse=True)

    return popular_items
