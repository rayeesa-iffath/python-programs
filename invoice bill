snacks = ["Chips", "Chocolate", "Juice", "Biscuit", "Sandwich"]
prices = [20, 50, 30, 10, 70]

cart = []   # To store selected snacks
bill = []   # To store selected snack prices

while True:
    print("\n====== SNACK MENU ======")

    # Display menu using list
    for i in range(len(snacks)):
        print(i + 1, ".", snacks[i], "- Rs.", prices[i])

    # User choice
    choice = int(input("Choose your snack number: "))

    # Check valid choice
    if choice >= 1 and choice <= len(snacks):
        cart.append(snacks[choice - 1])   # Add snack to cart
        bill.append(prices[choice - 1])   # Add price to bill

        print(snacks[choice - 1], "added to cart successfully!")
    else:
        print("Invalid choice!")
        continue

    # Ask to continue
    more = input("Do you want to add more snacks? (yes/no): ")

    if more.lower() != "yes":
        break


# Final Invoice
print("\n========= YOUR SNACK CART =========")

for i in range(len(cart)):
    print(cart[i], "- Rs.", bill[i])

print("----------------------------------")
print("Total Snacks Bought :", len(cart))
print("Total Amount        : Rs.", sum(bill))
print("----------------------------------")

confirm = input("Confirm Order? (yes/no): ")

if confirm.lower() == "yes":
    print("Order Placed Successfully!")
    print("Enjoy your snacks 😋")
else:
    print("Order Cancelled")
