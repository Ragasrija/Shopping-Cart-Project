# shopping_cart.py

# Products list
products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500}
]

# Initialize cart
cart = []

# View Products
def view_products():
    print("\nAvailable Products:")
    for p in products:
        print(f"{p['id']}. {p['name']} - ₹{p['price']}")

# Add to Cart
def add_to_cart():
    if len(cart) >= 8:
        print("Cart limit reached (max 8 items).")
        return
    try:
        product_id = int(input("Enter Product ID to add: "))
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Quantity must be at least 1.")
            return
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            print("Invalid Product ID.")
            return
        for item in cart:
            if item["id"] == product_id:
                item["quantity"] += qty
                print(f"Updated {item['name']} quantity to {item['quantity']}.")
                return
        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": qty
        })
        print(f"Added {product['name']} x{qty} to cart.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# View Cart
def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    print("\nYour Cart:")
    total = 0
    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
    print(f"Total: ₹{total}")

# Update Cart
def update_cart():
    if not cart:
        print("Cart is empty.")
        return
    try:
        product_id = int(input("Enter Product ID to update: "))
        new_qty = int(input("Enter new quantity: "))
        for item in cart:
            if item["id"] == product_id:
                if new_qty > 0:
                    item["quantity"] = new_qty
                    print(f"Updated {item['name']} quantity to {new_qty}.")
                else:
                    cart.remove(item)
                    print(f"Removed {item['name']} from cart because quantity was set to {new_qty}.")
                return
        print("Product not found in cart.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Remove from Cart
def remove_from_cart():
    if not cart:
        print("Cart is empty.")
        return
    try:
        product_id = int(input("Enter Product ID to remove: "))
        for item in cart:
            if item["id"] == product_id:
                cart.remove(item)
                print(f"Removed {item['name']} from cart.")
                return
        print("Product not in cart.")
    except ValueError:
        print("Invalid input. Enter numbers only.")

# Checkout
def checkout():
    if not cart:
        print("Cart is empty.")
        return
    print("\nCheckout Summary:")
    view_cart()
    print("Thank you for shopping with us!")
    cart.clear()

# ===== Menu loop =====
while True:
    print("\n===== Shopping Cart =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Update Cart")
    print("5. Remove from Cart")
    print("6. Checkout")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_products()
    elif choice == "2":
        view_products()
        add_to_cart()
    elif choice == "3":
        view_cart()
    elif choice == "4":
        update_cart()
    elif choice == "5":
        remove_from_cart()
    elif choice == "6":
        checkout()
    elif choice == "7":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-7.")
