from datetime import datetime
from list import get_items

# Simple mapping of months/festivals to item categories
festival_map = {
    "monsoon": ["cold", "cough", "fever"],
    "rakhi": ["gifts", "vitamin", "fever"],
    "diwali": ["pain relief", "digestive"],
    "winter": ["pain relief", "vitamin"]
}

def get_trending_items():
    current_month = datetime.now().month

    # Infer season/festival
    if current_month in [7, 8]:  # July, August
        season = "monsoon"
    elif current_month == 10:   # October
        season = "diwali"
    elif current_month == 11:   # November
        season = "winter"
    else:
        season = "rakhi"  # default case

    season_tags = festival_map.get(season, [])

    # Sample mapping of keywords to items (this can be improved with real data)
    keyword_map = {
        "Paracetamol": ["fever"],
        "Dolo 650": ["fever", "cold"],
        "Cetrizine": ["cold", "allergy"],
        "Digene": ["digestive"],
        "Vitamin C": ["vitamin"],
        "Pain Balm": ["pain relief"]
    }

    results = []
    for item in get_items():
        tags = keyword_map.get(item["name"], [])
        match = any(tag in season_tags for tag in tags)

        if match:
            results.append({
                "name": item["name"],
                "company": item["company"],
                "expiry": item["expiry"],
                "efficiency": item["efficiency"],
                "suggested_for": season.title()
            })

    return results
