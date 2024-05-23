import random

a = [
    "Honey never spoils.",
    "A group of giraffes is called a tower.",
    "A group of frogs is called an army.",
    "A group of apes is called a shrewdness.",
    "A group of crows is called a murder.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries aren't.",
    "An octopus has three hearts.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "A group of flamingos is called a 'flamboyance.'",
    "The shortest war in history lasted 38 minutes.",
    "Bees can fly higher than Mount Everest.",
    "Humans and giraffes have the same number of neck vertebrae.",
    "There are more stars in the universe than grains of sand on all the world's beaches."
]

def fun_fact(a): #creating a fun_fact function
    print(random.choice(a))

def main(): #creating main function
    fun_fact(a)

if __name__ == "__main__":
    main()
