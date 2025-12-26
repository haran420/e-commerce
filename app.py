from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


class Product:
    def __init__(self, pid, name, price, image, category, extra):
        self.pid = pid
        self.name = name
        self.price = price
        self.image = image
        self.category = category
        self.extra = extra


products = {
    1: Product(1, "Laptop", 55000, "laptop.png", "Electronics", "2 Years Warranty"),
    2: Product(2, "Smartphone", 30000, "phone.jpg", "Electronics", "1 Year Warranty"),
    3: Product(3, "T-Shirt", 1200, "tshirt.webp", "Clothing", "Size: S M L"),
    4: Product(4, "Jeans", 2500, "jeans.jpg", "Clothing", "Size: 32"),
}

cart = {}


# WELCOME SCREEN
@app.route("/")
def welcome():
    return render_template("welcome.html")

# PRODUCT HOME
@app.route("/shop")
def home():
    cart_count = sum(cart.values())
    return render_template(
        "home.html",
        products=products.values(),
        cart_count=cart_count
    )

@app.route("/add/<int:pid>")
def add_to_cart(pid):
    if pid in products:
        cart[pid] = cart.get(pid, 0) + 1
    return redirect(url_for("home"))

@app.route("/remove/<int:pid>")
def remove_item(pid):
    if pid in cart:
        del cart[pid]
    return redirect(url_for("view_cart"))

@app.route("/cart")
def view_cart():
    items = []
    total = 0

    for pid, qty in cart.items():
        product = products[pid]
        cost = product.price * qty
        total += cost
        items.append((product, qty, cost))

    return render_template("cart.html", items=items, total=total)

@app.route("/checkout")
def checkout():
    cart.clear()
    return "<h2>Order placed successfully ✅</h2><a href='/'>Go Home</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
