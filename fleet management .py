
#ena poribohon

class company:
 def __init__(self,name,address):
  self.name=name
  self.address=address 
  self.bus=[]
  self.routes=[]
  self.fare=[]
  self.counter=[]
  self.driver=[]
  self.manager=[]
  self.supervisor=[]

class driver:
 def __init__(self,name,age,experience):
  self.name=name
  self.age=age
  self.experience=experience 
  print(f'name: {self.name} age: {self.age} experience: {self.experience}')
class counter:
 def __init__(self):
  pass
 def purchase_ticket(self,start,end):
   pass

class passenger:
  pass

class manager:
 pass 
 

Nozu_mia=driver('Nozu Mia',45,7)




