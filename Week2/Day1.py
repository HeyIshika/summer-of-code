# print('First Name:');
# firstName = input();
# print('Middle Name:');
# middleName = input();
# print('Last Name:');
# lastName = input();
# print('Hello ' + firstName + ' ' +middleName+' '+lastName);


# Finding frequency distribution of alphabets 

filename = r"C:\Users\Ishika Paul\Desktop\New folder\alice in wonderland.txt"
file = open(filename , "r")
raw = file.read()
frequency = { }
for line in raw:
	if line.isalpha():
			count = frequency.get(line.lower(),0)
			frequency[line.lower()] = count + 1  


	frequency_list = frequency.keys()


for line in frequency_list:
	print (line, frequency[line])

