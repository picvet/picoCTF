#! /usr/bin/python

import codecs

# function to convert hex value to ASCII 
# equivalent

def hex_conversion(hex_string):
    string_bytes = bytes(hex_string, encoding='utf-8')

    binary_string = codecs.decode(string_bytes, "hex")
    return str(binary_string, 'utf-8')

# function to convert octal value to ASCII
# equivalent

def octal_conversion(oct_string):
    str_converted = ''
    for oct_char in oct_string.split(' '):
        str_converted += chr(int(oct_char, 8))
    return str_converted

# function to convert from bin to ASCII
# equivalent

def conversion(value):
    binary_int = int(value, 2);
     
    # Getting the byte number
    byte_number = binary_int.bit_length() + 7 // 8
     
    # Getting an array of bytes
    binary_array = binary_int.to_bytes(byte_number, "big")
     
    # Converting the array into ASCII text
    ascii_text = binary_array.decode()
     
    # Getting the ASCII value
    print(ascii_text)

# main method
if __name__ == '__main__':

    # take binary input from user and print
    bin_string = input('Enter binary:')

    conversion(bin_string.replace(' ', ''))

    # take octal input and convert
    oct_string = input('Enter octal:')

    print(octal_conversion(oct_string))

    # take hex input and convert
    hex_string = input('Enter hex:')

    print(hex_conversion(hex_string))

