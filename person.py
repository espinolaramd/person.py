#Diego Espinola
#11.14.19
#creating a person class

class person():

    def __init__(self,first,last,age,color):
        self.first = first
        self.last = last
        self.age = age
        self.color = color

    def desription(self):
        print(f"My name is  {self.first}{self.last}")
        print(f"I am {self.age}")
        print(f"My favorite color is {self.color}")

    def birthday(self):
        self.age = self.age + 1
        print(f"In May 10th is my birthday and I will be {self.age}")

    def ask_to_sum(self):
        x = int(input("Think about one number and write the number here"))
        y = int(input("Now write a second number here"))
        self.answer= x + y
        print(f"""Oh, I am very good guessing numbers, if I add the two numbers you 
are thinking the answer is {self.answer}""")
