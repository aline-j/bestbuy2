import store
import products

# Initialize store inventory with a list of products
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)


def show_menu():
    """
    Displays the main store menu to the  user.
    """
    print("\nStore Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_all_products():
    """
    Lists all active products in the store along with their price and quantity.
    """
    print("------")
    active_products = best_buy.get_all_products()
    for i, product in enumerate(active_products):
        print(f"{i + 1}. ", end="")
        product.show()
    print("------")


def show_total_quantity():
    """
    Displays the total quantity of all active products in the store.
    """
    total_quantity = best_buy.get_total_quantity()
    print(f"\nTotal quantity of all active products: {total_quantity}")


def make_order():
    """
    Allows the user to make an order by selecting products and quantities.
    Processes the order and prints the total payment.
    Handles invalid inputs and exceptions gracefully.
    """
    print("------")
    active_products = best_buy.get_all_products()
    for i, product in enumerate(active_products):
        print(f"{i + 1}. ", end="")
        product.show()
    print("------")
    print("When you want to finish order, enter empty text.")

    order = []

    while True:
        product_choice = input("Which product # do you want? ").strip()
        if product_choice == "":
            break
        if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(active_products):
            print("Invalid product number. Try again.")
            continue

        selected_product = active_products[int(product_choice) - 1]

        quantity_input = input("What amount do you want? ").strip()
        if quantity_input == "":
            break
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Invalid quantity. Try again.")
            continue

        quantity = int(quantity_input)

        # Check limit for LimitedProduct
        if isinstance(selected_product, products.LimitedProduct) and quantity > selected_product.maximum:
            print(f"Cannot buy more than {selected_product.maximum} items of '{selected_product.name}' per order.")
            continue

        # Add valid selection to order list
        order.append((selected_product, quantity))
        print("Product added to list!\n")

    # Finalize and process the order
    if order:
        try:
            total_price = best_buy.order(order)
            print("********")
            print(f"Order made! Total payment: ${total_price}")
        except ValueError as error:
            print(f"Order failed: {error}")
    else:
        print("No products ordered.")


def start():
    """
    Launches the interactive store menu loop.
    Users can list products, check total quantity, make orders, or quit.
    """
    while True:
        show_menu()
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            list_all_products()
        elif choice == "2":
            show_total_quantity()
        elif choice == "3":
            make_order()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Run the application if the script is executed directly
if __name__ == "__main__":
    start()
