#Trinity Saunders
#class section 14816
#9/28/2023
#help from TA Lucas Mach and Zoe Brown over Slack

def hex_char_decode(digit):
    hex_char = "0123456789abcdefABCDEF" #Decodes a single hexadecimal digit and returns its value.
    if digit in hex_char[0:10]:
        return int(digit)  #if the first character in the variable is a integer it should return a number val
    elif digit in hex_char[0:16]:
        return 10 + hex_char[10:16].index(digit) #should give a decimal value
    else:
        return 10 + hex_char[16:22].index(digit)


def hex_string_decode(hex):   #Decodes an entire hexadecimal string and returns its value.
    hex = hex.lower()
    decimal_value = 0
    if hex.startswith("0x"):
        hex = hex[2:]
    for i in range(len(hex)):
        decimal_value += hex_char_decode(hex[i]) * (16 ** (len(hex) - int(i) - 1))     # Adds the decimal value of the
        # current character to the decimals values result
    return decimal_value  # Returns the decimal result



def binary_string_decode(binary):
    decimal_value = 0
    if binary.startswith("0b"):
        binary = binary[2:]
    for i in range(len(binary)):
        decimal_value += int(binary[i]) * (2 ** (len(binary) - i - 1))
    return decimal_value




def binary_to_hex():
    decimal_value = binary_string_decode(binary) #converts binary to decimal
    hex = ""
    while decimal_value > 0:
        hex = "0123456789ABCDEF"[decimal % 16] + hex #Add the hexadecimal character representing the remainder
        # of decimal divided by 16 to the beginning of the hex string
        decimal_value = decimal_value // 16 #divies bc of the 16 character rule
    return hex #returns the hex result



def decode_menu(): #makes the menu when called
    print("\nDecoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal"
          "\n4. Quit")



if __name__ =="__main__":

    run = True

    while run:
        decode_menu()
        selection = int((input("Please enter an option: ")))
        if selection == 1:
            num_string = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(num_string)
            print("\nResult:", result, "\n")
        elif selection == 2:
            binary_string = input("\nPlease enter the numeric string to convert: ") #takes the binary string
            result = binary_string_decode(binary_string) #should decode the binary
            print("\nResult:", result, "\n")
        elif selection == 3:
            binary_string = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(binary_string)
            print("\nResult:", result, "\n")
        elif selection == 4:
            print("Goodbye!")
            exit()
        else:
            print('Invalid Operation. Please try again.')
