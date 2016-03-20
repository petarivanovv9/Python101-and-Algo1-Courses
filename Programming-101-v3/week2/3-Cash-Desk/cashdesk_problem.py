class Bill:

    def __init__(self, amount):
        self.amount = amount
        # Bill.money_holder[self] = 0

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __int__(self):
        # return int(self.amount)
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.amount)

    def total(self):
        return self.amount

    def get_bills(self):
        return str(self)

    def to_dictionary(self):
        return {self.amount: 1}


a = Bill(10)
b = Bill(5)
c = Bill(10)

print (a)
print (int(a) == 10)
print (str(a) == "A 10$ bill")

print (a == b)
print (a == c)

money_holder = {}

money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print (money_holder)

print (10 * '-')


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return len(self.bills)

    def get_bills(self):
        return [str(x) for x in self.bills]

    def total(self):
        return sum([int(x) for x in self.bills])

    def to_dictionary(self):
        return {int(x): self.bills.count(x) for x in self.bills}


values = [10, 20, 50, 100]

# bills is a list of Bill objects
bills = [Bill(value) for value in values]

# batch is a Batchbill object that has a value - list of Bill objects
batch = BatchBill(bills)

for bill in batch:
    print (bill)

print (len(batch))
print (batch.total())

print (10 * '-')


class CashDesk:

    def __init__(self):
        self.cashdesk_money = 0
        self.bills_dict = {}

    def take_money(self, money):
        self.cashdesk_money += money.total()
        converted_money = money.to_dictionary()

        for key in converted_money.keys():
            if int(key) in self.bills_dict.keys():
                self.bills_dict[key] += converted_money[key]
            else:
                self.bills_dict[key] = converted_money[key]

    def total(self):
        return self.cashdesk_money

    def inspect(self):
        to_pairs = [(key, self.bills_dict[key])
                    for key in self.bills_dict.keys()]
        to_pairs.sort()

        for elem in to_pairs:
            print ("{}$  bills - {}".format(elem[0], elem[1]))

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print ("We have a total of {}$ in the desk.".format(desk.total()))

desk.inspect()
