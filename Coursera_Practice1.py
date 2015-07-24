# Practice page for Python course

print ('Hi There!')

#Get the name of the file from the user and open it
name=raw_input("Enter your file: ") #Show it the file
handle=open(name, "r") #set an object that is the opened file
text=handle.read() #set an object that is the opened and read file
words=text.split() #set an object that is the opened, read, split file

#Count the frequency of words in the file
counts=dict() #Make function Counts that is an empty dictionary
for word in words: #For every word inside the split text
	counts[word]=counts.get(word,0)+1 #when you find the word, iterate the number
#Then add the word and the count as a pair in the empty dictionary of "counts"

#Identify the most commonly appearing word
bigcount=None #Set this variable as empty to start
bigword=None #set this variable as empty to start
for word,count in counts.items(): 
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count

#Give the final most common word and its count
print bigword,bigcount