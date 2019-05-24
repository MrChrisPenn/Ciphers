code_list = []
a_2_z = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
z_2_a = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
encoded_message = ""


def encode():
    answer = input("Ok... Please type the message you want to code!")
    for x in range (len(answer)):

        index = a_2_z.index(answer[x])
        code_list.append(z_2_a[index])
    

def encode_right_shift():
    answer = input("Ok... Please type the message you want to code!")
    no_of_places = int(input("now... please type in the number of places you wish to shift to the right"))
    
    for x in range (len(answer)):
        if no_of_places == 1:
            if answer[x] == "z":
                replacement = "a"
                code_list.append(replacement)
            else:
                index = a_2_z.index(answer[x])
                replacement =  a_2_z[index+no_of_places]
                code_list.append(replacement)


print("Hello user.")

answer = int(input("How do you wish to encode a message 1)Simple reverse cipher 2)Ceaser cipher right shift"))

if answer == 1:#simple cipher

    while True:

        #print("Ok... Please type the message you want to code!")
        encode()
        print(encoded_message.join(code_list))
        answer = input("Do you want to continue?")

        if answer == "yes":
            print("As you wish!")
            print(code_list, "Coded message is now reset")
            code_list.clear()
            print(code_list)
            
        else:
            break

elif answer == 2:#Ceaser right shift

    while True:
        encode_right_shift()
        print(code_list)
        print(encoded_message.join(code_list))
        answer = input("Do you want to continue?")

        if answer == "yes":
            print("As you wish!")
            print(code_list, "Coded message is now reset")
            code_list.clear()
            print(code_list)
            
        else:
            break
    


