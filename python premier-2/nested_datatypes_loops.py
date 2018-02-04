food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
for hungry in food["vegetables"]:
	print("My favorite vegetable is " + hungry)

print()
for hungry2 in food["desserts"]:
	print("My favorite dessert is " + hungry2)

print()
cars={"sports":{"Volkswagen":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
for auto in cars["sports"]:
	print("My favorite sports " + auto + " car is a " + cars["sports"][auto])
	
print()	
for auto2 in cars["classic"]:
	print("My favorite " + auto2 + " classic car is " + cars["classic"][auto2])

print()	
dessert={"iceCream":["Rocky Road","strawberry","Pistachio Cashew","Pecan Praline"]}
for afterfood in dessert["iceCream"]:
	print("My favourite dessert is " + afterfood)

print()
soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"good for you"}}
for drinksoup in soup["soup"]:
 print("my favorite " + drinksoup + " soup is " + soup["soup"][drinksoup])