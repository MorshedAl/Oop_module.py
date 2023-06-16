# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class 
class Gadget: 
 def __init__(self, brand, price, color, origin) -> None: 
  self.brand = brand 
  self.price = price 
  self.color = color 
  self.origin = origin 
 
 def run(self): 
  return f'=>{self.brand}' 


class Laptop(Gadget): 
 def __init__(self,brand,price,color,origin,memory,ssd):
   super().__init__(brand, price, color, origin) 
   self.memory=memory
   self.ssd=ssd
    
 def __repr__(self):
  return f'{self.brand},{self.price},{self.color},{self.origin},{self.ssd},{self.memory}'


class Phone(Gadget): 
 def __init__(self, brand, price, color, origin, dual_sim) -> None: 
  self.dual_sim = dual_sim 
  super().__init__(brand,price,color,origin) 
 
 def phone_call(self, number, text): 
  return f'Sending SMS to: {number} with: {text}' 

 def __repr__(self) -> str: 
  return f'phone: {self.brand} price:{self.price} dualsim:{self.dual_sim}' 


class Camera(Gadget): 
 def __init__(self,brand,price,color,origin,pixel):
   self.pixel=pixel
   super().__init__(brand,price,color,origin)
   
 def __repr__(self):
   return f'{self.brand},{self.pixel}'





my_phone = Phone('iphone', 120000, 'silver', 'china', True)
# my_phone.phone_call()
#print(my_phone.brand)
print(my_phone)
print(my_phone.run())

my_laptop=Laptop('samsung',153000,'black','korea',4,250)
print(my_laptop)
print(my_laptop.run())

my_camera=Camera('piko',5000,'black','usa',1200)
print(my_camera)
print(my_camera.color)

