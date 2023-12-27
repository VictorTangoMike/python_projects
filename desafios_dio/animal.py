caracteristicas = []

a = input().lower()
caracteristicas.append(a)

b = input().lower() 
caracteristicas.append(b)

c = input().lower()
caracteristicas.append(c)


animais = {
    "aguia" : ["vertebrado", "ave", "carnivoro"],
    "pomba" : ["vertebrado", "ave", "onivoro"],

    "homem" : ["vertebrado", "mamifero", "onivoro"],
    "vaca" : ["vertebrado", "mamifero", "herbivoro"],

    "pulga" : ["invertebrado", "inseto", "hematofago"],
    "lagarta" : ["invertebrado", "inseto", "herbivoro"],

    "sanguessuga" : ["invertebrado", "anelideo", "hematofago"],
    "minhoca" : ["invertebrado", "anelideo", "onivoro"]
    }

for animal, caracteristicas_animal in animais.items():
    if all(caracteristica in caracteristicas_animal for caracteristica in caracteristicas):
        print(animal)