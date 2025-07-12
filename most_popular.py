from items import get_items

def get_most_popular_items():
    popular_items = []

    for item in get_items():
        sell = item['sell']
        total = item['total_purchase']
        efficiency = item['efficiency']

        popularity_score = (sell / total) * 100  # Higher is better

        popular_items.append({
            "name": item["name"],
            "company": item["company"],
            "sell": sell,
            "total": total,
            "efficiency": efficiency,
            "popularity_score": popularity_score
        })

    # Sort items by popularity score descending
    popular_items.sort(key=lambda x: x["popularity_score"], reverse=True)

    return popular_items
