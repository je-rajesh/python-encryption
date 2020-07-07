""" Written By Rajesh Chaurasiya <i.raj3sh@gmail.com>
    This file contains all the function requires to encrypt a file.

    @parameters: any valid python string:
    @returns : encrypted message:
 """

# ENCRYPTING A STRING INTO STREAM OF 1'S AND 0'S.
# function takes a python string into input and convert it into stream of 0's and 1's.
#
# IMPORTING LIBRARIES NEEDED FOR THIS
import binascii


def convert_to_binary(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def split_string_to_words(binary_string):
    """splits the string into words"""
    temp_list = []
    for i in range(0, len(binary_string), 32):
        word = binary_string[i: i+32]
        temp_list.append(word)
    return temp_list


def encrypt_word(word):
    """encrypt the word using even-odd substitution method"""
    decimal_value = int(word, 2)
    p = 0
    l = len(word)
    enc_word = ''
    while p < l:
        temp = decimal_value % 2
        if temp == 0:
            decimal_value = decimal_value // 2
            enc_word = enc_word + '0'
        elif temp == 1:
            decimal_value = (decimal_value + 1) // 2
            enc_word = enc_word + '1'
        p += 1
    return enc_word


def encrypt_word_list(word_list):
    """takes a list of 4-bit word, encrypt the words and returns them."""
    temp_word = ''
    temp_list = []
    for word in word_list:
        temp_word = encrypt_word(word)
        temp_list.append(temp_word)

    return temp_list


def binary_to_encrypted_char(encrypted_string):
    encrypted_message = ''
    for i in range(0, len(encrypted_string), 8):
        character = encrypted_string[i: i+8]
        encrypted_message += chr(int(character, 2))
    return encrypted_message


def encrypt(string):
    """ actually encrypt the message
    @parameter: any string
    @returns : an encrypted message in binary format
    """
    binary_string = str(convert_to_binary(string))
    word_list = split_string_to_words(binary_string)
    encrypted_word_list = encrypt_word_list(word_list)
    encrypted_string = ''
    for word in encrypted_word_list:
        encrypted_string += word
    encrypted_message = binary_to_encrypted_char(encrypted_string)
    return encrypted_message
    # encrypted_message = text_from_bits(encrypted_string)


# print(encrypt('Local Area Network'))
