from random import randint

def random_num():
    return randint(0, 10)


while True:
	print('Guess the number:', end= " ")
	input_no = int(input())
	output=random_num()
	print("input no " + str(input_no) + " output " + str(output))
	
	if input_no != output:
		print("Wrong, try again!")

	else:
		print("Correct")
		break



	