# program to find Tuple-Based Product Catalogue

number_of_products = int(input("How many products? "))
products = []

for i in range(number_of_products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity in stock: "))

    product = (name, price, quantity)
    products.append(product)

minimum_stock = int(input("Enter the minimum stock quantity: "))

for product in products:
    name, price, quantity = product
    stock_value = price * quantity

    print(name, "stock value:", stock_value)

    if quantity < minimum_stock:
        print("More", name, "should be ordered")
    else:
        print(name, "stock is enough")