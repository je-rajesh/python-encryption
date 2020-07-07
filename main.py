# read a file in from terminal here.
import encryption
input_stream = open("input.txt", "r")
output_stream = open("output.txt", "w")

# reading a file and saving it into a variable.
string = input_stream.read()
# print(string)


#ENCRYPT THE MESSAGE AND SAVE IT TO THE ANOTHER FILE 
encrypted_message = encryption.encrypt(string)
print("encrypted message is:",encrypted_message, sep=" ")
# SAVE IT TO THE FILE 
output_stream.write(encrypted_message)
output_stream.close()
input_stream.close()
# print(binary_list)

# NOW TO DECRYPT THE ENCRYPTED MESSAGE: 
import decryption 
input_stream = open("output.txt", "r+")
decrypt_stream = open("decrypt.txt", "w")

string = input_stream.read()
# print(string)
decrypted_message = decryption.decrypt(string)
print('decrypted message is: ',decrypted_message, sep=" ")




