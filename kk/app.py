from flask import Flask, render_template,request,redirect
from datetime import datetime

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return redirect("/product")

@app.route("/my-name")
def my_name():
    return"My name is power ranger."

@app.route("/current")
def current():
        return f"Now is {datetime.now()}"

# products = []

# @app.route("/product", methods=["GET", "POST"])
# def create_product():
#     if request.method == "POST":
#         name = request.form.get("name")
#         price = request.form.get("price")
#         products.append({"name": name, "price": price})
#         print(products)
        
#     return render_template("product.html")
    

# if __name__ == "__main__":
#     app.run(debug=True)


@app.route('/') #root
def home():
    return redirect("/product_list")

products = []

@app.route("/product",methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        products.append({"name": name, "price": price})
        print(products)
        return redirect("/product_list")
        
    return render_template("product.html")

@app.route("/product_list")
def list_products():
    return render_template("product_list.html", proudct_list=products)


@app.route("/product/<index>",methods=["POST"])
def delete_product(index):
    if index != "" and index.isdigit():
        index = int(index)
    else:
        index = 0
        
    if index >= 0 and index < len(products):
        products.pop(index)
        
    return redirect("/product_list")

@app.route("/product/edit/<index>", methods=["GET", "POST"])
def edit_product(index):
    if index != "" and index.isdigit():
        index = int(index)
    else:
        return redirect("/product_list")

    current = products[index]
    if request.method == "GET":
        return render_template("product_edit.html", current=current)
    else:
        current["name"] = request.form.get("name")
        current["price"] = request.form.get("price")
        return redirect("/product_list")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/greeting/<name>")
def greet(name):
    address = request.args.get("address")
    township = request.args.get("township")
    return render_template("greet.html", user_name=name, address=address, township=township)

if __name__ == "__main__":
    app.run(debug=True)