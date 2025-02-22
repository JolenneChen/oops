# create a class called as animals it should have at least 6 properties and 5 funcitons and a constructor
# using the about class create atleast 5 objects and all all the functions

class Animals :
    breed = "Poodle"
    color = "Brown"
    eyes = "round"
    name = "Kiyomi"
    height = "super duper short"
    legs = 4

    def __init__(self,breed,color,eyes,name,height,legs):
        print("\nWhat Kiyomi is doing every second\n")
        self.breed = breed
        self.color = color
        self.eyes = eyes
        self.name = name
        self.height = height
        self.legs = legs
        self.speak = {}

    def speak(self,languages):
        print(f"{self.speak} is {language}\n")
        
    def sleep(self):
        print(f"{self.name} is sleeping\n")
        
    def pee(self):
        print(f"{self.name} is peeing\n")
        
    def play(self):
        print(f"{self.name} is playing\n")
        
    def bite(self):
        print(f"{self.name} is biting something\n")

class Dog(Animals):
     def __init__(self,name,age,species):
         super().__init__(name,age,species)


if __name__ == "__main__":
    dog = Dog("Kiyomi","3 years", "Poodle,")
    dog.speak()

    dog1 = Dog("Bally","1 month","Pomeranian")
    dog.sleep()

    cat = Animals("Siamese cat","white and black","sharp","John","slightly tall",4)
    cat.sleep()

    turtle = Animals("Spotted turtle","dark green","Large eyes","Peter","as tall as a turtle",4)
    turtle.pee()

    sheep = Animals("Damara sheep","white","Round","mary","average height",4)
    sheep.play()

    
