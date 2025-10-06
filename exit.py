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
