# this was written for main function <i.raj3sh@gmail.com>

# converting a string into bits
def convert_to_binary(sentence):
    bin_data = ''.join('{0:08b}'.format(ord(x), 'b') for x in sentence)
    return bin_data


# converting an array back to the original sentense
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def binaryToString(bin_data):
    str_data = ''
    for i in range(0, len(bin_data), 8):
        print(bin_data)
        temp_data = int(bin_data[i:i+8])
        decimal_data = binaryToDecimal(temp_data)
        str_data += chr(decimal_data)
        # print(str_data)
    return str_data


# encrypting 8 bit strings .
def encrypt(binary):
    # print(binary)
    if(binary % 2 == 0):
        binary += 1
    else:
        binary -= 1
    return binary

# encrypt the str_data


def encrypt_data(bin_data):
    str_data = ''
    for i in range(0, len(bin_data), 8):
        temp_data = bin_data[i:i+8]
        print(temp_data)
        enc_data = encrypt(temp_data)
        str_data += chr(enc_data)
    return str_data


def int2bytes(i):
    import binascii
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)


def __main__():
    sentence = 'rajesh kumar chaurasiya'
    converted_string = convert_to_binary(sentence)
    encrypted_string = text_from_bits(converted_string)
    return encrypted_string


print(__main__())
# print(binaryToString(res))
# <i.raj3sh@gmail.com>


# FROM ENCRYPTION.PY 
# def convert_to_binary(sentence):
#     """ takes a string and converts it into a valid string. """
#     bin_data = ''.join('{0:08b}'.format(ord(x), 'b') for x in sentence)
#     return bin_data



# def int2bytes(i):
#     """converts binary to the ascii character codes"""
#     hex_string = '%x' % i
#     n = len(hex_string)
#     return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


# def text_from_bits(bits, encoding='utf-16', errors='surrogatepass'):
#     """converts to ascii codes to the characters"""
#     n = int(bits, 2)
#     return int2bytes(n).decode(encoding, errors)