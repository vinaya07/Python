"""
Case study: A Go Card account maintains a balance that may be spent on public transport. Users may request a statement that shows all transactions. The only transactions are to top up the account with some positive number of dollars, and to take a ride costing some dollars and cents.
The goal for this exercise is to develop a class for a Go Card Account. The class will be tested by a program that simulates transactions, like this:
Creating account. Input initial balance: 100
? r 3.50
? r 10.90
? b
Balance = $85.60
? t 20
? x gghhg
Bad command.
? t
Bad command.
? q
Statement:
event			amount ($) 	balance ($)
Initial balance				       100.00
Ride	3.50	     96.50
Ride	10.90	     85.60
Top up	20.00	     105.60
Final balance	     105.60
where:
•	r number simulates a ride costing number dollars;
•	t number simulates a top up of number dollars;
•	b requests the current balance; and
•	q ends input and prints a statement.
Bad inputs are to be reported and ignored.

Let us consider the design for a class that represents a Go Card account. To design a class, we consider what services the object(s) must provide (its methods), and what data needs to be stored in the object(s) to support those services. Questions:
•	What is a good name for a class that represents a Go Card account?
o	Be descriptive of what the class represents. Don’t include the word “class” in the name.
•	What services should be provided?
o	A constructor (__init__) is required to set up the account with an initial balance.
o	It needs to record the amount each ride costs. A method that accepts the amount as a parameter is required.
o	It needs to record the amount for each top-up. A method that accepts the amount as a parameter is required.
o	It needs to be able to report the current balance at any time. A method that returns this is required.
o	A method is required print out a statement of all of the transactions.
We can see from the output of the proposed program that the class needs to store the details of every transaction in order.
•	What data is required to be stored in the object to enable those services?
o	So that a method can return the current balance at any time, it would be useful have a field for the current balance.
o	So that the full statement can be printed, the object must store the amount of each transaction, in order. What data type can grow and keep multiple values in the order they are added?
"""


class GoCardAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.bal = initial_balance
        self.transactions = [("Initial balance", initial_balance)]

    def ride(self, amount):
        self.balance -= amount
        self.transactions.append(("Ride", amount))

    def top_up(self, amount):
        self.balance += amount
        self.transactions.append(("Top up", amount))

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print("Statement:")
        print("{:<15} {:<12} {:<12}".format("Event", "Amount ($)", "Balance ($)"))
        for event, amount in self.transactions:
            if event == "Initial balance":
                print("{:<15} {:<12} {:<12.2f}".format(event, "", amount))
            elif event == "Ride":
                self.bal -= amount
                print("{:<15} {:<12} {:<12.2f}".format(event, amount, self.bal))
            else:
                self.bal += amount
                print("{:<15} {:<12.2f} {:<12.2f}".format(event, amount, self.bal))
            print("Final balance    {:<12}".format(round(self.bal, 2)))


def main():
    initial_balance = int(input("Creating account. Input initial balance: "))
    account = GoCardAccount(initial_balance)

    while True:
        command = input("? ")
        if command == "q":
            account.print_statement()
            break
        elif command == "b":
            print("Balance = ${:.2f}".format(account.get_balance()))
        elif command.startswith("r"):
            try:
                amount = float(command[2:])
                account.ride(amount)
            except ValueError:
                print("Bad command.")
        elif command.startswith("t"):
            try:
                amount = float(command[2:])
                account.top_up(amount)
            except ValueError:
                print("Bad command.")
        else:
            print("Bad command.")


if __name__ == "__main__":
    main()
