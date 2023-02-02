# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.hidden_name = name
        self.hidden_symbol = symbol
        self.hidden_number = number

    # 10.7에 따라
    @property
    def name(self):
        return self.hidden_name

    @property
    def symbol(self):
        return self.symbol

    @property
    def number(self):
        return self.hidden_number

    # 10.6 때...
    # def dump(self):
    #    print(self.name, self.symbol, self.number)

    # 10.7에 따라 바뀜
    def __str__(self):
        print(self.name, self.symbol, self.number)


# 10.5 // 10.7
hydro = Element('Hydrogen', 'H', 1)

# 10.6
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': '1'}
# hydro.dump()

# 10.7
print(hydro)
