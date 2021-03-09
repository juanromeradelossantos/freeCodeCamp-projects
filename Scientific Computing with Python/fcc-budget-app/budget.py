class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        s = ''
        s += '{:*^30}\n'.format(self.name)
        for i in self.ledger:
            if len(i['description']) > 23:
                tmp = i['description'][0:23]
            else:
                tmp = i['description']
            s += '{:23}'.format(tmp)

            if len(str(i['amount'])) > 7:
                tmp = str(i['amount'])[0:7]
            else:
                tmp = str(i['amount'])
            s += '{:>7.2f}\n'.format(float(tmp))
            
        s += 'Total: {:.2f}'.format(self.get_balance())
        return s

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to {}".format(category.name)):
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True


def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    withdrawals = []
    perc = []
    total = 0

    for i in range(len(categories)):
        withdrawals.append([])
        for j in categories[i].ledger:
            if j['amount'] < 0:
                withdrawals[i].append(j['amount'])
                total -= j['amount']

    for i in withdrawals:
        perc.append(int(sum(i)/total*(-100)))

    for i in range(100,-1,-10):
        res += '{:>3}'.format(str(i)) + '|'
        for j in perc:
            if i <= j:
                res += ' o '
            else:
                res += '   '
        res += ' \n'

    res += ' '*4 + '-'*3*len(categories) + '-' + '\n'
    max_len = max([len(i.name) for i in categories])

    for i in range(max_len):
        res += ' '*4
        for j in range(len(categories)):
            if i < len(categories[j].name):
                res += ' {} '.format(categories[j].name[i])
            else:
                res += ' '*3
        if i != max_len-1:
            res += ' \n'
        else:
            res += ' '

    return res
