class Budget:
    
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount

        return f"you have deposited {self.balance} in {self.name} budget"

    def withdraw(self, amount):
        if self.balance < amount:
            return "......insufficient balance......"
        else:
            self.balance = self.balance - amount

            information = "------------------------------- \n"
            information += "Your withdrawal was successful \n"
            information += f"Your new balance is #{self.balance} in {self.name} budget"

            return information

    def categoryBalances(self):
        information = f"The balance for category {self.name} is #{self.balance}"

        return information

    def transferingBalance(self, amount, category):
        if self.balance < amount:
            return "......insufficient balance......"
        else:
            self.balance -= amount
            category.balance += amount

            information = "------------------------------- \n"
            information += "Category transfer successful \n"
            information += f"The balance for {self.name} is now #{self.balance}\n"
            information += f"The balance for {category.name} is now #{category.balance}"

            return information


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

food.deposit(3000)
clothing.deposit(5000)
entertainment.deposit(4000)


#CREATING A BUDGET CLASS

print(food.name)
print("-------------------------------")
print(clothing.name)
print("-------------------------------")
print(entertainment.name)
print("-------------------------------")

#DEPOSITING FUNDS

print(food.deposit(3000))
print("-------------------------------")
print(clothing.deposit(5000))
print("-------------------------------")
print(entertainment.deposit(4000))

#WITHDRAWING FUNDS

print(food.withdraw(1000))
print(clothing.withdraw(3000))
print(entertainment.withdraw(1500))

#COMPUTING CATEGORY BALANCES

print("-------------------------------")
print(food.categoryBalances())
print("-------------------------------")
print(clothing.categoryBalances())
print("-------------------------------")
print(entertainment.categoryBalances())

#TRANSFERING BALANCE AMOUNTS (CLOTHING AND FOOD)

print(clothing.transferingBalance(1000, food))

