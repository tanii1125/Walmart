from flask import Flask,render_template
from waitress import serve
from items import get_items
from deals import get_deals
from predict import get_predictions, get_zero_stock_items, get_restock_by_date_items  # ✅
from trending import get_trending_items
from most_popular import get_most_popular_items

app=Flask(__name__)

@app.route('/')
def index():
    out_of_stock_items = get_zero_stock_items()
    count = len(out_of_stock_items)
    return render_template("index.html", out_of_stock_count=count)
@app.route('/display_items')
def items():
    item_list = get_items()
    return render_template("items.html", items=item_list)
@app.route('/deals')
def deals():
    deal_items = get_deals()
    return render_template("deals.html", deals=deal_items)
@app.route('/restore_predict')
def predict():
    data = get_predictions()
    out_of_stock = get_zero_stock_items()
    restock_by_date = get_restock_by_date_items()  # ✅
    return render_template("predict.html", predictions=data, out_of_stock=out_of_stock, restock_by_date=restock_by_date)

@app.route('/trending')
def trending():
    trending_items = get_trending_items()
    return render_template("trending.html", items=trending_items)
@app.route('/most_popular')
def most_popular():
    popular_items = get_most_popular_items()
    return render_template("most_popular.html", items=popular_items)

##festive pop-up
if __name__=="__main__":
    serve(app, host='0.0.0.0', port=4000)