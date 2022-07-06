### Первый вариант ###
class Animal:
    def __init__(self, Name, Color, Voice):
        self.Name = Name
        self.Color = Color
        self.Voice = Voice
    def return_voice(self):
        return f"It says {self.Voice}."

Cow = Animal('Jessy', 'black', 'muuu')
Cat = Animal('Thomas', 'grey', 'meow')
Dog = Animal('Butcher', 'brown', 'gav-gav-gav')

print(Cow.return_voice())

print(f"{Cow.Name} is {Cow.Color}. It says {Cow.Voice}.")
print(f"{Cat.Name} is {Cat.Color}. It says {Cat.Voice}.")
print(f"{Dog.Name} is {Dog.Color}. It says {Dog.Voice}.")


### Второй вариант ###
#class Animal:
#    def __init__(self, name, color):
#        self.name = name
#        self.color = color

#    def give_voice(self):
#        print(f'{self.name} is {self.color}. It says {self.give_voice}')

#class Voice:
#    def __init__(self, voice):
#        self.voice = voice

#    def says(self):
#        print(f'{self.name} is {self.color}. It says {self.voice}')

#class Cat(Animal, Voice):
#    def __init__(self, color, name, voice):
#       Animal.__init__(self, color, name)
#        Voice.__init__(self, voice)

#class Cow(Animal, Voice):
#    def __init__(self, color, name, voice):
#        Animal.__init__(self, color, name)
#        Voice.__init__(self, voice)

#class Dog(Animal, Voice):
#    def __init__(self, color, name, voice):
#        Animal.__init__(self, color, name)
#        Voice.__init__(self, voice)
#    def give_voice(self):
#        print(f'{self.name} is {self.color}. It says {self.give_voice}')


#caat = Cat('Thomas', 'Grey', 'meow')
#coow = Cow('Felicia', 'Black', 'muuu')
#doog = Dog('Butcher', 'Brown', 'gav-gav-gav')
#caat.give_voice()
#caat.says()
#coow.says()
#doog.says()

