#data scrubber or sum

print("Hellow user this is the Data scrubber")

raw_data = input("Please input your raw data. Press \"q\" to exit: ")

while not raw_data == "q":

    colon_position = raw_data.find(":")

    if colon_position != -1: 

        clean_number_string = raw_data[colon_position + 1:]
        clean_number_string = float(clean_number_string)
        print(f"Your scrubbed data is: {clean_number_string:,.2f}")
        raw_data = input("Please input your raw data. Press \"q\" to exit: ")

    else:
    
        print("Error: Invalid data log format! Missing colon ':'.")
        raw_data = input("Please input your raw data. Press \"q\" to exit: ")
        

print("Bye.")