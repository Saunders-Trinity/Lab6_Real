# Trinity Saunders
#With help from professor Daniel Davis  office hrs
#class section 14816
from console_gfx import ConsoleGfx

def count_runs(flat_data):
    program_count = 1
    program_runs = 0
    for i in range(1, len(flat_data)):
        if flat_data[i - 1] == flat_data[i]:
            program_count += 1
            if program_count == 2:
                program_runs += 1
            if program_count == 15:
                program_count == 0
                program_runs += 1
        elif flat_data[i - 1] != flat_data[i]:
            program_runs += 1
            program_count = 1
    if flat_data[-1] != flat_data[-2]:
        program_runs += 1

    elif flat_data[-1] == flat_data[-2]:
        program_count += 1
        if program_count <= 15:
            program_runs = program_runs
        elif program_count > 15:
            program_runs += 1

    return program_runs



def get_decoded_length(rle_data):
    rle_decoded_len = 0
    for i in range(0, len(rle_data), 2):
        if i % 2 == 0:
            rle_decoded_len += rle_data[i]
    return rle_decoded_len



def encode_rle(flat_data):
    program_count = 1
    encoded_rle = []
    for i in range(1, len(flat_data)):
        if flat_data[i - 1] == flat_data[i]:
            program_count += 1
            if i == len(flat_data) - 1:
                encoded_rle.append(program_count)
                encoded_rle.append(flat_data[i])
            if program_count == 15:
                encoded_rle.append(program_count)
                encoded_rle.append(flat_data[i])
                program_count = 0
        elif flat_data[i - 1] != flat_data[i]:
            encoded_rle.append(program_count)
            encoded_rle.append(flat_data[i - 1])
            program_count = 1

        else:
            program_count = 1
    if flat_data[-1] != flat_data[-2]:
        encoded_rle.append(1)
        encoded_rle.append(flat_data[-1])

    return encoded_rle



def decode_rle(rle_data):
    decoded_rle = []
    for i in range(0, len(rle_data), 2):
        for times in range(0, rle_data[i]):
            decoded_rle.append(rle_data[i + 1])
    return decoded_rle



def to_rle_string(rle_data):
    rle_string = ""
    char_values = {'0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   'a': 10,
                   'b': 11,
                   'c': 12,
                   'd': 13,
                   'e': 14,
                   'f': 15}
    for i in range(1, len(rle_data), 2):
        rle_string += str(rle_data[i - 1]) + str(char_values[rle_data[i]])
        if i + 1 < len(rle_data):
            rle_string += ":"
    return rle_string



def to_hex_string(data):
    to_hex = ""
    char_values = {0: '0',
                   1: '1',
                   2: '2',
                   3: '3',
                   4: '4',
                   5: '5',
                   6: '6',
                   7: '7',
                   8: '8',
                   9: '9',
                   10: 'a',
                   11: 'b',
                   12: 'c',
                   13: 'd',
                   14: 'e',
                   15: 'f'}
    for i in range(0, len(data)):
        hex_string = char_values[data[i]]
        to_hex += hex_string
    return to_hex



def string_to_rle(rle_string):
    str1 = None
    str2 = None
    i = 0
    str_list = []
    program_result = []
    char_values = {'0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   'a': 10,
                   'b': 11,
                   'c': 12,
                   'd': 13,
                   'e': 14,
                   'f': 15}
    for char in rle_string:
        if char == ":":
            if len(str_list) == 3:
                str1 = str(str_list[0]) + str(str_list[1])
                str2 = str(str_list[2])
                program_result.append(int(str1))
                program_result.append(int(str2))
                str_list.clear()

            elif len(str_list) == 2:
                str1 = str(str_list[0])
                str2 = str(str_list[1])
                program_result.append(int(str1))
                program_result.append(int(str2))
                str_list.clear()

        else:
            str_list.append(char_values[char])

    if len(str_list) == 3:
        str1 = str(str_list[0]) + str(str_list[1])
        str2 = str(str_list[2])
        program_result.append(int(str1))
        program_result.append(int(str2))
        str_list.clear()

    elif len(str_list) == 2:
        str1 = str(str_list[0])
        str2 = str(str_list[1])
        program_result.append(int(str1))
        program_result.append(int(str2))
        str_list.clear()

    return program_result



def string_to_data(data_string):
    data = []
    char_values = {'0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   'a': 10,
                   'b': 11,
                   'c': 12,
                   'd': 13,
                   'e': 14,
                   'f': 15}

    for value in data_string:
        hex_string = char_values[value]
        data.append(hex_string)
    return data



def menu(): #prints menu when called
    print(f"RLE Menu\n--------\n0.Exit\n1.Load File\n2.Load Test Image\n3.Read RLE String\n4.Read RLE Hex String"
          "\n5.Read Data Hex String\n6.Display Image\n7.Display RLE String\n8.Display Hex RLE Data"
          "\n9.Display Hex Flat Data")



if __name__ == '__main__':
    image = None
    current_data = None

    print("\nWelcome to the RLE image encoder!")  #zybooks output
    print("\nDisplaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    while True:
        menu()
        option = input("\nSelect a Menu Option: ")

        if option == '0':
            exit()

        elif option == '1':
            load_file = input("Enter name of file to load: ")
            image = ConsoleGfx.load_file(load_file)

        elif option == '2':
            image = ConsoleGfx.test_image
            print("Test image data loaded.")

        elif option == '3':
            current_data = input("Enter an RLE string to be decoded: ")
            current_data = current_data.lower()
            current_data = decode_rle(string_to_rle(current_data))

        elif option == '4':
            current_data = input("Enter the hex string holding RLE data: ")
            current_data = current_data.lower()
            current_data = decode_rle(string_to_data(current_data))

        elif option == '5':
            current_data = input("Enter the hex string holding flat data: ")
            current_data = string_to_data(current_data)

        elif option == '6':
            print("Displaying image...")
            ConsoleGfx.display_image(image)

        elif option == '7':
            image_output = to_rle_string(encode_rle(current_data))
            print("RLE representation:", image_output)

        elif option == '8':
            image_output = to_hex_string(encode_rle(current_data))
            print("RLE hex values: ", image_output)

        elif option == '9':
            image_output = to_hex_string(current_data)
            print("Flat hex values: ", image_output)

        else:
            print("Error! Invalid Input.")