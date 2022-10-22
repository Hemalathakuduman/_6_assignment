class dog:
        def __init__(self,name,age,coat_color):                           # constructor
            self.name = name
            self.age = age
            self.coat_color = coat_color
        def description(self, name, age):
            print(self.name)
            print(self.age)
        def get_info(self, coat_color):
            print(self.coat_color)

class JackRussellTerrier(dog):
    def sex(self, sex):
        print(sex)
    def nature(self, nautre):
        print(nautre)

class Bulldog(dog):
     def sex(self, sex):
        print(sex)
     def nature(self, nature):
        print(nature)

dog_obj = dog("dora", 2, "black")  
dog_obj.description("dora", 2)
dog_obj.get_info("brown")

JackRussellTerrier_obj = JackRussellTerrier("dora", 2, "black")
JackRussellTerrier_obj.sex("female")
JackRussellTerrier_obj.nature("Not friendly")

Bulldog_obj = Bulldog("dora", 2, "black")
Bulldog_obj.sex("male")
Bulldog_obj.nature("friendly")



