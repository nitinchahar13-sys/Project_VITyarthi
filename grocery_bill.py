import datetime

items = {
    "rice": 50,
    "sugar": 40,
    "wheat": 45,
    "milk": 30,
    "oil": 120,
    "salt": 20,
    "bread": 25,
    "butter": 90
}

cart = {}

def show_items():
    print("\n------ AVAILABLE ITEMS ------")
    for item, price in items.items():
        print(f"{item} : ₹{price}")
    print("-----------------------------")

def add_to_cart():
    while True:
        item = input("\nEnter item name (or 'done' to finish): ").lower()
        if item == "done":
            break
        if item not in items:
            print("❌ Item not found! Try again.")
            continue
        qty = int(input("Enter quantity: "))
        cart[item] = cart.get(item, 0) + qty
        print(f"✔ Added {qty} x {item}")

def generate_bill():
    print("\n============ BILL ============")
    print("Date:", datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S"))
    print("--------------------------------")

    total = 0
    for item, qty in cart.items():
        price = items[item] * qty
        total += price
        print(f"{item.capitalize()}   x{qty}   = ₹{price}")

    gst = total * 0.05  
    grand_total = total + gst

    print("--------------------------------")
    print(f"Subtotal: ₹{total}")
    print(f"GST (5%): ₹{gst:.2f}")
    print(f"Total Payable: ₹{grand_total:.2f}")
    print("============ THANK YOU ==========\n")


print("========== GROCERY BILLING SYSTEM ==========")
show_items()
add_to_cart()
generate_bill()
