# Dictionary containing alphabet letters as keys and morse letters
alphabet_dict = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }


def encode_sentence(word_to_decode):
    # Every letter in word_to_encode going to the alphabet dictionary
    for letter in word_to_decode:
        if letter == " ":
            print(" ", end="/ ")
        elif letter != " ":
            print(alphabet_dict[letter], end="")


def decode_sentence(word_to_encode):
    # Reverse keys and values from alphabet_dict
    reverse_alpha_dict = {morse: letter for letter, morse in alphabet_dict.items()}

    # Add few items to dictionary in order to help decoding
    reverse_alpha_dict["/"] = " "
    reverse_alpha_dict["/ "] = " "
    reverse_alpha_dict[" "] = ""

    # Checking if sentence has the space at the end
    if word_to_encode[-1] != " ":
        word_to_encode += " "

    # List that will contain words from word_to_encode
    words_in_password = []
    whole_word = ""

    # Looping through letters in word_to_encode
    for letter in word_to_encode:
        # Creating morse words out of letters,
        # if letter is space, append created word to list
        if letter != " ":
            whole_word += letter
        if letter == " ":
            words_in_password.append(whole_word)
            whole_word = ""

    # Finding every morse word in the dictionary
    for morse_word in words_in_password:
        morse_word += " "
        print(reverse_alpha_dict[morse_word], end="")


# USER MENU

mode = input("Type decode or encode : ")

if mode == "decode" or mode == "Decode":
    password = input("Type word you want to decode : ")
    decode_sentence(password)

if mode == "encode" or mode == "Encode":
    password = input("Type word you want to encode : ")
    password = password.upper()
    encode_sentence(password)
