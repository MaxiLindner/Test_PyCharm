def name_to_bin(input_name):
    name_as_number = []
    output = ""
    for x in input_name.casefold():
        name_as_number.append(ord(x) - 96)
    pari_bit = 0
    for i in range(0, 3):
        pari_bit = (pari_bit + name_as_number[i]) % 2
        output += str(bin(name_as_number[i])[2:].zfill(5))
    print(output + str(pari_bit))

if __name__ == '__main__':
    name_to_bin((input("Your name:")))
