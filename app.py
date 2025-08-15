from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Needed for sessions

# Sample product list
products = [
    {"id": 1, "name": "T-Shirt", "price": 500},
    {"id": 2, "name": "Jeans", "price": 1200},
    {"id": 3, "name": "Shoes", "price": 2000}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Get cart from session
    cart = session.get('cart', [])
    # Add selected product
    for product in products:
        if product["id"] == product_id:
            cart.append(product)
            break
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item["price"] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/clear_cart')
def clear_cart():
    session['cart'] = []
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)