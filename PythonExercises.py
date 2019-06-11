# --------------------------------------- Exercise 7.1 ----------------------------------------------
'''try:
	user_input = input("Enter a file name: ")
except:
	print("Type file not valid")
	exit()
fhand = open(user_input)
for line in fhand:
	line = line.rstrip().upper()
	print(line)'''
# ------------------------------- Exercise 7.2 & Exercise 7.3 ---------------------------------------
'''user_input = input("Enter a file name: ")
try:
	fhand = open(user_input)
except:
	if user_input == "na na boo boo":
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
		exit()
	print("File cannot be opened:",user_input)
	exit()

count = 0
total = 0
for line in fhand:
	line = line.rstrip()
	if line.startswith("X-DSPAM-Confidence: "):
		line = line[20:]
		total = total+float(line)
		count = count + 1
	else:
		continue

print("Average spam confidence: ",total/count)'''
# --------------------------------------- Exercise 8.1 ----------------------------------------------
#-----> Chapter 8 exercises use LIST data structure.
'''numbers = [1,3,5,7,9]

def chop(x):
	del x[0]
	del x[3]
	return None

chop(numbers)
print(numbers) # Parte A do exercicio'''

'''def middle(x):
	y = x[1:4]
	return y

print(numbers)
print(middle(numbers))''' # Parte B do exercicio	
# --------------------------------------- Exercise 8.2 ----------------------------------------------
'''fhand = open('mbox-short.txt')
count = 0

for line in fhand:
	words = line.split()
	# print 'Debug:', words
	if len(words) == 0 : continue
	if words[0] != 'From' : continue
	print(words[2])'''
# --------------------------------------- Exercise 8.4 ----------------------------------------------
'''structure = list()
fhand = open("romeo.txt")

for line in fhand:
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word not in structure:
				structure.append(word)

structure.sort()
print(structure)'''
# --------------------------------------- Exercise 8.5 ----------------------------------------------
#Searches in a file the lines that start with 'From', split that lines in individual words and print the
#word that contains email address
'''count = 0
file = input("Enter a file name:")
try:
	fhand = open(file)
except:
	print("Your entered file is not valid")

for line in fhand:
	if not line.startswith("From"): continue
	line = line.rstrip()
	words = line.split()
	count = count + 1
	print(words[1])

print("There were",count,"lines in the file with From as the first word")'''
# --------------------------------------- Exercise 8.6 ----------------------------------------------
#Prints the grater and the smaller numbers of a series typed by the user, when the same types 'done'
'''numbers = list()
while True:
	input_user = input("Enter a number:")
	if input_user == "done" : break
	numbers.append(input_user)

print(max(numbers))
print(min(numbers))'''
# --------------------------------------- Exercise 9.1 ----------------------------------------------
#Writes a program that reads the words in words.txt and stores them as keys in a dictionary
'''structure = dict()
fhand = open("romeo.txt")

for line in fhand:
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word not in structure:
			structure[word] = 1
		else:
			structure[word] += 1

print(structure)
print('and' in structure)'''
# --------------------------------------- Exercise 9.2 ----------------------------------------------
#Categorizes each mail message by which day of the week the commit was done and keep a running count of
#each of the days of the week. -----> Chapter 9 exercises use DICTIONARY data structure.
'''days = dict()
userFile = input("Enter your file:")
try:
	fhand = open(userFile)
except:
	print("File not valid!!!")
	exit()

for line in fhand:
	line = line.strip()
	if not line.startswith("From "): continue
	words = line.split()
	days[words[2]] = days.get(words[2],0) + 1

print(days)'''
# ------------------------------- Exercise 9.3 & Exercise 9.4 ---------------------------------------
#Reads through a mail log and builds a histogram using a dictionary to count how many messages have 
#come from for each mail address and figure out who has the most messages in the file
'''emails = dict()
key = None
greaterValue = None
userFile = input("Enter your file:")
try:
	fhand = open(userFile)
except:
	print("File not valid!!!")
	exit()

for line in fhand:
	line = line.strip()
	if not line.startswith("From ") or line.startswith("From:"): continue
	words = line.split()
	emails[words[1]] = emails.get(words[1],0) + 1
for k,v in emails.items():   #iterates through the items of the dictionary 'emails'
	if greaterValue == None or v > greaterValue:
		key = k
		greaterValue = v

print(emails)
print("Most messages come from:",key,"with:",greaterValue,"emails")'''
# --------------------------------------- Exercise 9.5 ----------------------------------------------
#Records the domain name where the message was sent from and prints out the content of the dictionary
'''emails = dict()
userFile = input("Enter your file:")
try:
	fhand = open(userFile)
except:
	print("File not valid!!!")
	exit()

for line in fhand:
	line = line.strip()
	if not line.startswith("From ") or line.startswith("From:"): continue
	words = line.split()
	word = words[1]
	leftDelimeter = word.find('@')                 #Finds @ character's index in word
	RightDelimeter = word.find(' ',leftDelimeter)  #Finds ' ' character's index in word using leftDelimeter as starting index
	emails[word[leftDelimeter+1:RightDelimeter]] = emails.get(word[leftDelimeter+1:RightDelimeter],0) + 1

print(emails)'''






























