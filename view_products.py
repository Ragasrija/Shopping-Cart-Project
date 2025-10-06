# View Products
def view_products():
    print("\nAvailable Products:")
    for p in products:
        print(f"{p['id']}. {p['name']} - ₹{p['price']}")
