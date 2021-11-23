class Cash:
    def __init__(self, value, quantity):    
        self.value = value
        self.quantity = quantity
        self.total = round((quantity * value), 2)

cash50 = Cash(50, 6)
print(cash50.total)


coin50 = Cash(0.50, 7)
print(coin50.total)