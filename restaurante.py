class Command:
   def __init__(self,quantity,stock):
       self.quantity = quantity
       self.stock = stock

   def execute(self):
      if self.check_stock():
         return self.calculate()
      else:
         raise Exception('No stock')

   def check_stock(self):
      return self.stock >= self.quantity
    
   def calculate(self):
      raise Exception('Override this method, please')

class FrenchFries(Command):
   def calculate(self):
       return 5000 * self.quantity


class Hamburguer(Command):
    def calculate(self):
        return 15000 * self.quantity


class Soda(Command):
    def calculate(self):
        return 3000 * self.quantity


class Combo(Command):
   def __init__(self,quantity):
       self.quantity = quantity
       self.products = []

   def add_product(self, product):
       self.products.append(product)

   def execute(self):
      ammount = 0
      rangeproducts = len(self.products)
      for i in range (rangeproducts):
         ammount += self.products[i].execute()
      return ammount




#UI
ammount = 0

default_fries_stock = 100
default_burguer_stock = 100
default_soda_stock = 100


order = int(input("""What would you like?
1 - French fries
2 - Hamburguer
3 - Soda
4 - Combo básico
5 - Como niño (no disponible)
"""))
qty = int(input("""How many?
"""))

try:
   if order == 1:
      ammount = FrenchFries(qty,default_fries_stock).execute()
   elif order == 2:
      ammount = Hamburguer(qty,default_burguer_stock).execute()
   elif order == 3:
      ammount = Soda(qty,default_soda_stock).execute()
   elif order == 4:
      combo = Combo(qty)
      combo.add_product(Hamburguer(qty,default_fries_stock))
      combo.add_product(Soda(qty,default_burguer_stock))
      combo.add_product(FrenchFries(qty,default_soda_stock))
      ammount = combo.execute()
   else:
      print("Try it again :/")


   print("It is: \n $ " + str(ammount))
except:
   print('Error, intente de nuevo')

