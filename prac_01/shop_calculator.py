
def main():
    num_items = -1
    while num_items < 0:
        try:
            num_items = int(input("Number of items: "))
            if num_items < 0:
                print("Invalid number of items!")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    prices = []
    for i in range(num_items):
        while True:
            try:
                price = float(input("Price of item {}: ".format(i + 1)))
                if price < 0:
                    print("Price cannot be negative!")
                else:
                    prices.append(price)
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    total_price = calculate_total_price(num_items)
    print("Total price for {} items is ${:.2f}".format(num_items, total_price))


def calculate_total_price(prices):
    total_price = sum(prices)
    if total_price > 100:
        total_price = 90/100 * total_price
    return total_price


main()
