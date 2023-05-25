string = input('your string: ')
removing = input('characters to remove: ')

for char in removing:
	string = string.replace(char, '')

print(string)
