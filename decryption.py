"""Written By: Rajesh Chaurasiya <i.raj3sh@gmail.com> with love.
    this file contains all function required for decrypting a message encrypted by even-odd substitution method. Fill free to fork me on github @je-rajesh
"""


def proper_binary(binary_string):
    """this function converts a binary string into a size of multiple of 8 by adding extra 0's at beginning."""
    size = len(binary_string)
    if size % 8 == 0:
        return binary_string
    else:
        proper_size = ((size + 8) // 8) * 8
        required_zero = proper_size - size
        zero = ''
        for i in range(required_zero):
            zero += '0'
        return zero + binary_string


def convert_to_binary(string):
    """converts a ascii string into binary string"""
    binary_string = ''
    for i in string:
        binary_string += proper_binary(bin(ord(i))[2:])
    return binary_string


def split_string_to_words(binary_string):
    """returns list of binary words of size 32bit"""
    word_list = []
    for i in range(0, len(binary_string), 32):
        word = binary_string[i:i+32]
        word_list.append(word)
    return word_list


def to_binary(decimal):
    """converts the no into binary string"""
    temp = bin(decimal)[2:]
    return proper_binary(temp)


def decrypt_word(word):
    """decryption takes place from LSB to MSB"""
    t = 1
    for i in range(len(word)-1, -1, -1):
        if word[i] == '1':
            t = t*2 - 1
        elif word[i] == '0':
            t = 2*t
    return to_binary(t)


def decrypt_word_list(word_list):
    """decrypt a list of words into decrypted list"""
    temp_list = []
    for word in word_list:
        temp_list.append(decrypt_word(word))
    return temp_list


def convert_to_decrypted_message(bit_string):
    actual_message = ''
    for i in range(0, len(bit_string), 8):
        word = bit_string[i:i+8]
        letter = chr(int(word, 2))
        actual_message += letter
    return actual_message


def decrypt(string):
    """this function takes the string and decrypt that into original message"""
    binary_string = str(convert_to_binary(string))
    word_list = split_string_to_words(binary_string)
    decrypted_word_list = decrypt_word_list(word_list)
    original_bit_string = ''
    for word in decrypted_word_list:
        original_bit_string += word
    # return original_bit_string
    return convert_to_decrypted_message(original_bit_string)


n2 = '01110001011111011111101111001001'
n1 = '11111001001110010000100111001101'
n3 = '01001101111110110111100101011001'
n4 = '10001001000100011101000101011001'
n5 = '1110100110110001'

n = n1 + n2 + n3 + n4 + n5

temp = 'ù9	Íq}ûÉMûyYÑY©±'
# print(decrypt(temp))
