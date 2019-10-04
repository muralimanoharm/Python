class Person:
    def __init__(self,name,age):
        self.age = age
        self.name = name
        
    def GetDetails(self):
        print("My name is ",self.name," and my age is ",self.age)

    def SetNewDetails(self,name,age):
        print("Updating New details")
        self.name=name
        self.age=age
        
person = Person("Murali",25)

person.GetDetails()

person.SetNewDetails("Murali Manohar",25)

person.GetDetails()
