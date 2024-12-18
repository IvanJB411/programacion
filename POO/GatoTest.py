from plain_cat import PlainCat

gojo =PlainCat("Gojo", "macho")
rika = PlainCat("Rika", "hembra")
felipe = PlainCat("Felipe", "macho")

print("Hola gatito")
felipe.miau()
print("Te voy a acariciar")
felipe.purr()
print("Toma una manzana")
felipe.eat("manzana")
print("Pues toma pescado")
felipe.eat("pescado")

print("Felipe pelea con los otros")
felipe.fight_whit("rika")
felipe.fight_whit("gojo")
