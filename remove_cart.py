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
