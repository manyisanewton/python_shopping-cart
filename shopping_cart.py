# Function to display items in the shopping cart
def display_cart(cart):
    if not cart:  # If the cart is empty, tell the user
        print("Your cart is empty.")
    else:
        print("\nShopping Cart:")
        total_price = 0  # Variable to keep track of total cost
        for index, item in enumerate(cart, start=1):  # Loop through each item in the cart
            print(f"{index}. {item['name']}: ${item['price']:.2f}")  # Show item number, name, and price
            total_price += item['price']  # Add price to total
        print(f"Total price: ${total_price:.2f}")  # Show total cost of all items


# Main function that runs the shopping cart program
def main():
    cart = []  # Start with an empty cart
    
    while True:  # Keep showing menu until the user decides to quit
        print("\nShopping Cart Application")
        print("1. Add item to cart")
        print("2. Display cart")
        print("3. Remove item from cart")
        print("4. Quit")

        choice = input("Choose an option: ")  # Get user's choice

        if choice == '1':  # If the user wants to add an item
            item_name = input("Enter the name of the item: ")  # Get item name
            try:
                item_price = float(input("Enter the price of the item: "))  # Get item price
                cart.append({'name': item_name, 'price': item_price})  # Add item to cart
                print(f"{item_name} has been added to the cart.")
            except ValueError:  # If the user enters something that isn't a number
                print("Invalid price! Please enter a number.")

        elif choice == '2':  # If the user wants to see what's in the cart
            display_cart(cart)

        elif choice == '3':  # If the user wants to remove an item
            if not cart:  # Check if the cart is empty
                print("Your cart is already empty.")
            else:
                display_cart(cart)  # Show the cart before removing
                try:
                    item_index = int(input("Enter the item number you want to remove: ")) - 1  
                    if 0 <= item_index < len(cart):  # Check if the number is valid
                        removed_item = cart.pop(item_index)  # Remove the item
                        print(f"Removed: {removed_item['name']}")  
                    else:
                        print("Invalid item number.")  # If the number is out of range
                except ValueError:  # If the user enters something that isn't a number
                    print("Please enter a valid number.")

        elif choice == '4':  # If the user wants to quit
            print("Exiting the application. Goodbye!")
            break  # Exit the loop and end the program

        else:  # If the user enters something that isn't 1, 2, 3, or 4
            print("Invalid choice, please select a valid option.")


# Run the main function when the program starts
if __name__ == "__main__":
    main()
