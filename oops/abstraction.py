class Animals():   
    def types(self):   
        pass  
  
class Dog(Animals):   
    def types(self):   
        print("which is so sweet")   
class Giraffe(Animals):   
    def types(self):   
        print("long neck")   
class Cat(Animals):   
     def types(self):   
        print("which is rugged ")
class Snake(Animals):   
    def types(self):
        print("very bad")    
t1= Dog ()   
t1.types()   
t2 = Giraffe()   
t2.types()   
t3= Cat()   
t3.types()   
t4 = Snake()   
t4.types()  