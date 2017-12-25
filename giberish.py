
print('THE GIBERISH MAKER')
print("STARTING..")
while True:
	try:
		import random
		import pyperclip
		weestring=""
		string=""
		alphabet=["a","b","c","e","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		hey=int(input("type a number ,then press enter."))
		hey=hey+1
		wee=input("do you want an infinate 'wee!' (well untill you press ctr+c...)? ")
		
		
		
		if wee=="yes":
			may=input("would you want to copy the wee?")
			while True:
				weestring=str(weestring+"wee ")
				print(weestring)
				if may=="yes":
					pyperclip.copy(weestring)
			
		for i in range(1,hey):
			hey=int(hey)
			a=random.choice(alphabet)
			string=str(string+a)
		print(string)
		pyperclip.copy(string)
		print('sucsessfully copyed string to clipboard!')
	
	except:
		print("there was an error(or maybe a monster eating this computer) :(")
