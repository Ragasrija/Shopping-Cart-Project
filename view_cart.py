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
