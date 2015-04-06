import random
import string
import csv


def weasel():

	print('''This program will generate a set of randomized passwords to your specifications, and save them for you to import into the password manager of your choice.''')
	print("")

	a=raw_input('Do you want symbols? ')

	while (a.upper()=='Y' or a.upper()=="YES" or a.upper()=="N" or a.upper()=="NO")==False:
		a=raw_input('Do you want symbols? Yes or no? ')

	b=raw_input('Do you want ambiguous looking characters? ')

	while (b.upper()=='Y' or b.upper()=="YES" or b.upper()=="N" or b.upper()=="NO")==False:
		b=raw_input('Do you want ambiguous looking characters? Yes or no? ')

	c=raw_input('What length would you like your passwords to be? Please give a numeral. ')
	while c.isdigit()==False:
		c=raw_input('What length would you like your passwords to be? Numeral answer required, for realz. ')
	d=raw_input('How many passwords do you want? Please give a numeral. ')
	while d.isdigit()==False:
		d=raw_input('How many passwords do you want? Numeral answer required, for realz. ')
	print("")
	
	c=int(c)
	d=int(d)


	if (a.upper()=="Y" or a.upper()=="YES") and (b.upper()=="Y" or b.upper()=="YES") :


		for i in range(d):
	
			p2=''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*?><~')for i in range(c))

			print p2
		
			outfile = open("passwords.csv","a")
			outfile.write(p2)
			outfile.write(','+'\r\n')
			outfile.close()

		print("")
		print (str(d)+" passwords done!")


	elif (a.upper()=="N" or a.upper()=="NO") and (b.upper()=="Y" or b.upper()=="YES"):


		for i in range(d):
	
			p2=''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')for i in range(c))

			print p2

			outfile = open("passwords.csv","a")
			outfile.write(p2)
			outfile.write(','+'\r\n')
			outfile.close()

		print("")
		print (str(d)+" passwords done!")


	elif (a.upper()=="Y" or a.upper()=="YES") and (b.upper()=="N" or b.upper()=="NO"):

		for i in range(d):
	
			p2=''.join(random.choice('23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz!@#$%^&*?><~')for i in range(c))

			print p2
		
			outfile = open("passwords.csv","a")
			outfile.write(p2)
			outfile.write(','+'\r\n')
			outfile.close()

		print("")
		print (str(d)+" passwords done!")
	



	elif (a.upper()=="N" or a.upper()=="NO") and (b.upper()=="N" or b.upper()=="NO"):

		for i in range(d):
	
			p2=''.join(random.choice('23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz')for i in range(c))

			print p2
		
			outfile = open("passwords.csv","a")
			outfile.write(p2)
			outfile.write(','+'\r\n')
			outfile.close()

		print("")
		print (str(d)+" passwords done!")
	

	print("")

	print("Your passwords have been saved to a file called passwords.csv.")


if __name__ == "__main__": weasel()

# Program generates multi character randomized passwords and 
# saves to external .csv. User chooses length, number of passwords, and 
# contents of passwords.

