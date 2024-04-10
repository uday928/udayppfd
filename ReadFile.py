number_of_words = 0
with open(r'C:\Users\Gandhi Uday\OneDrive\Desktop\Uday Works\visual works\Asme.txt','r') as file:
# with open(r'Text_file_Adress','r') as file:
	data = file.read()
	lines = data.split()
	number_of_words += len(lines)
print(number_of_words)
