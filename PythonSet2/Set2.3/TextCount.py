number_of_words = 0
with open(r'C:\Users\Gandhi Uday\Downloads\pyAssgn\pyAssgn\Set2.3\Asme.txt','r') as file:
	data = file.read()
	lines = data.split()
	number_of_words += len(lines)
print(number_of_words)
