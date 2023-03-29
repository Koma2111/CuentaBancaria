class CuentaBancaria:
    cuentas = []
def __init__(self,int_rate,balance): 
       self.int_rate =int_rate
       self.balance = balance
       CuentaBancaria.cuentas.append(self)

def depósito(self, amount):
      self.balance +=amount
      return self

def retiro(self, amount):
      if(self.balance - amount) >=0:
            self.balance -=amount
      else:
        print("Insuficciente,Fondo,cargando a $10 tarifa")
        self.balance +=(self.balance * self.int_rate)

def mostrar_info_cuenta(self):
  print(f"Balance:{self.balance}")
  return self
 
def generar_interés(self):
       if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

