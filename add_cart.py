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
