import csv

with open('CupcakeInvoices.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    orderList = []
    for row in reader:
        firstName, lastName, cupcakeType, quantity, price = row
        newRow = [firstName, lastName, cupcakeType, int(quantity), float(price)]
        orderList.append(newRow)


print('\nAll Orders')
for row in orderList:
    print(row)

print('\nCupcake Type Ordered')
for row in orderList:
    print(row[2])

print('\nOrder Total')
for row in orderList:
    print(row[3] * row[4])
