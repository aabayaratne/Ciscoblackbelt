
strveg="My favorite vegetable is "
strdes="My favorite dessert is "

food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
print(strveg + food["vegetables"][0])
print(strveg + food["vegetables"][1])
print(strveg + food["vegetables"][2])
print(strveg + food["vegetables"][3])
print(strdes + food["desserts"][0])
print(strdes + food["desserts"][1])
print(strdes + food["desserts"][2])

print()
strsport="My favorite sports car is a "
cars={"sports":{"Volkswagen":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
print(strsport + " Volkswagen " + cars["sports"]["Volkswagen"])
print(strsport + " Dodge " + cars["sports"]["Dodge"])
print(strsport + " Chevy " + cars["sports"]["Chevy"])

strclassic="My favorite classic car is a "
print(strclassic + " Mercedes-Benz " + cars["classic"]["Mercedes-Benz"])
print(strclassic + " Toyota " + cars["classic"]["Toyota"])
print(strclassic + " Lincoln " + cars["classic"]["Lincoln"])

print()

strdesert="My favorite iceCream is "
dessert={"iceCream":["Rocky Road","strawberry","Pistachio Cashew","Pecan Praline"]}
print(strdesert + dessert["iceCream"][0])
print(strdesert + dessert["iceCream"][1])
print(strdesert + dessert["iceCream"][2])
print(strdesert + dessert["iceCream"][3])

print()

strsoup="My favorite soup is "
soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"good for you"}}
print(strsoup + soup["soup"]["tomato"])
print(strsoup + soup["soup"]["onion"])
print(strsoup + soup["soup"]["vegetable"])

