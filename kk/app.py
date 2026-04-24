from flask import Flask, render_template,request,redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("/product")

@app.route("/my-name")
def my_name():
    return"My name is power ranger."

@app.route("/current")
def current():
        return f"Now is {datetime.now()}"

products = []

@app.route("/product", methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        products.append({"name": name, "price": price})
        print(products)
        
    return render_template("product.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/greeting/<name>")
def greet(name):
    address = request.args.get("address")
    township = request.args.get("township")
    return render_template("greet.html", user_name=name, address=address, township=township)

if __name__ == "__main__":
    app.run(debug=True)