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