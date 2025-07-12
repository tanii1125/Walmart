from flask import Flask,render_template
from waitress import serve
from items import get_items
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/display_items')
def items():
    item_list = get_items()
    return render_template("items.html", items=item_list)
@app.route('/deals')
def deals():
     deal_items = get_deals()
    return render_template("deals.html", deals=deal_items)
@app.route('/restore_predict')
def restore():
    data = get_predictions()
    return render_template("predict.html", predictions=data)
@app.route('/trending')
def trending():
    trending_items = get_trending_items()
    return render_template("trending.html", items=trending_items)

##festive pop-up
if __name__=="__main__":
    serve(app, host='0.0.0.0', port=4000)