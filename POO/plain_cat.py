#Metodos hacer miau, ronrronear, comer y pelear
#Luego hacer prueba en GatoTest

class PlainCat:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


    def miau(self):

        """EL gato hace miau"""

        print(f"{self.name}: Miauuuu!!!")

    def purr(self):

        """El gato ronrronea"""

        print(f"{self.name}: Mrrrrrr!")

    def eat(self, food):

        """Hace que el gato coma la comida que le des"""

        if food == "pescado":
            print(f"{self.name}: Hmmm que rico")
        else:
            print(f"{self.name}: Yo solo como pescado")

    def fight_whit(self, opponent):

        """Hace que el gato pelee con otro gato. Si el gato es hembra, no pelea, si el gato es macho,
           si el oponente es macho, pelea, si es hembra, no pelea """

        if self.sex == "hembra":
            print(f"{self.name}: No me gusta pelear")
        elif opponent.sex == "hembra":
            print("No peleo con gatitas")
        else:
            print("ERROR")

