def is_palindrome(obj):
    obj = str(obj)
    obj_list = list(obj)
    obj_list_reversed = obj_list[::-1]

    return obj_list == obj_list_reversed


def generate_rotations(word):
    letters = list(word)
    string_rotations = []
    counter = len(letters)

    temp = letters
    while counter != 0:
        current_letter = temp.pop(0)
        temp.append(current_letter)
        word = "".join(temp)
        string_rotations.append(word)
        counter -= 1

    return string_rotations


def get_rotated_palindromes(string_rotations):
    is_empty = True

    for word in string_rotations:
        if is_palindrome(word) is True:
            print(word)
            is_empty = False

    if is_empty is True:
        print("NONE")


def main():
    user_input = input("Enter a string: ")

    string_rotations = generate_rotations(user_input)

    get_rotated_palindromes(string_rotations)


if __name__ == '__main__':
    main()
