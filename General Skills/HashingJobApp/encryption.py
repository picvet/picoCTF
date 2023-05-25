import hashlib

# text to encode
text = input('Enter text: ')

# encoding text using md5 hash
result = hashlib.md5(text.encode('utf-8')).hexdigest()

# printing the equivalent byte value
print(result)