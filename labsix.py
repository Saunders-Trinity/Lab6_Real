#Trinity Saunders

def decode(password):
    decoded_password = ""
    for num in password:
        og_password = int((str(num) - 3) % 10)
        decoded_password += og_password
    return password

def menu():
    print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n") #prints menu when called


def encode(first_password):  #adds the value of 3 to each integer and encodes the password
    encoded_password = ""
    for digit in first_password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

def decode(encoded_password): #subtracts 3 from each integer and decodes the encoded password
    decoded_password = ''
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        decoded_password += new_digit
    return decoded_password


if __name__ =="__main__":

    menu()
    option = input("\nPlease enter an option: ")



    take_num_input = False
    while not take_num_input:
        if option == '1':
            first_password = input("Please enter your password to encode: ")
            encoded_password = encode(first_password)
            print("\nYour password has been encoded and stored!")
        elif option == '2':
            decode_password = decode(encoded_password)
            print("\nThe encoded password is",encoded_password,"and the original pass word is",first_password,"\n")
        elif option == '3':
            exit()
        else:
            print("Invalid option, please enter 1-3.")

