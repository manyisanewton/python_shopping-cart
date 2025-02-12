


# python_Shopping Cart Application

## Overview
The **Shopping Cart Application** is a simple command-line program that allows users to manage a shopping cart. Users can add items, view their cart, remove items, and check out. The program ensures a smooth shopping experience by validating user inputs and displaying relevant information about the cart.

## Features
- **Add Items to Cart**: Users can add items by providing a name and price.
- **Display Cart**: The cart contents, including item names, prices, and total cost, are displayed.
- **Remove Items from Cart**: Users can remove items by selecting them from the displayed list.
- **Exit the Application**: Users can exit the program gracefully.

## Technologies Used
- **Python** (Version 3.x)

## How to Run the Program
1. Ensure you have Python installed (Version 3.x recommended).
2. Save the script as `shopping_cart.py`.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using the command:
   ```sh
   python shopping_cart.py
# usage 
--**When the program starts, the user is presented with a menu:
   Shopping Cart Application
1. Add item to cart
2. Display cart
3. Remove item from cart
4. Quit

Adding an Item: Select option 1, enter the item name and price.

Displaying the Cart: Select option 2 to view all items and total cost.

Removing an Item: Select option 3, choose an item number to remove.

Exiting the Application: Select option 4 to quit.

# Example session 
Shopping Cart Application
1. Add item to cart
2. Display cart
3. Remove item from cart
4. Quit
Choose an option: 1
Enter the name of the item: Apple
Enter the price of the item: 1.50
Apple has been added to the cart.

Choose an option: 2
Shopping Cart:
1. Apple: $1.50
Total price: $1.50

Choose an option: 3
Enter the item number you want to remove: 1
Removed: Apple

Choose an option: 4
Exiting the application. Goodbye!

# Error Handling

If the user enters a non-numeric value for the price, an error message is displayed.

If the user enters an invalid item number for removal, they are prompted again.

The program prevents removing items from an empty cart.

# License

This project is open-source and available under the MIT License.

# Author

Developed by [Newton Manyisa].

