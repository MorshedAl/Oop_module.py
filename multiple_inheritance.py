class Family:
 def __init__(self, address) -> None:
  self.address = address 
  print(self.address)

class School:
 def __init__(self, id, level) -> None:
  self.id = id
  self.level = level 
  print(self.level)

class Sports:
 def __init__(self, game) -> None:
  self.game = game 
  print(self.game)

class Student(Family, School, Sports):
 def __init__(self, address, id, level, game) -> None:
 
  super().__init__(address) #super ইউজ করলে একাধিক class এর প্রথমটিকে ইন্ডিকেইট করে।
  School.__init__(self,id, level) 
  Sports.__init__(self, game)
  




stu=Student('ctg',105,'ten','football')
print(stu)   
    
    
    