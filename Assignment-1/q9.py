class Product:
    def input(self):
        self.product_no = int(input("Enter product no: "))
        self.product_name = input("Enter product name: ")
        self.cost = int(input("Enter product cost: "))
        self.quantity = int(input("Enter product quantity: "))

    def calculator(self):
        self.total_amount = self.cost * self.quantity

    def display(self):
        print("Product No =", self.product_no)
        print("Product Name =", self.product_name)
        print("Cost =", self.cost)
        print("Quantity =", self.quantity)
        print("Total Amount =", self.total_amount)


pk = []

for i in range(3):
    print("\nEnter Product", i + 1)
    p = Product()
    p.input()
    p.calculator()
    pk.append(p)

high = pk[0]

for i in pk:
    if i.total_amount > high.total_amount:
        high = i

print("\nProduct with Highest Total Amount:")
high.display()
