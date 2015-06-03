def main():
    message = input("Enter an encrypted msg: ")

    length = len(message)

    if length % 2 != 0:
        bam = int(length / 2)
        first_part = message[:bam]
        second_part = message[bam + 1:]
    else:
        bam = int(length / 2)
        first_part = message[:bam]
        second_part = message[bam:]

    msg = second_part + first_part

    length_alphabet = int(msg.split('~')[0])

    length_key = int(msg.split('~')[2])

    alphabet = msg.split('~')[1][:length_alphabet]
    key = msg.split('~')[1][::-1][:length_key][::-1]
    encrypted_message = msg.split('~')[1][length_alphabet:len(msg.split('~')[1]) - length_key]

    resized_key = []
    j = 0

    for i in range(0, len(encrypted_message)):
        resized_key.append(key[j])

        if j + 1 == length_key:
            j = 0
        else:
            j += 1

    result = []

    for i in range(0, len(encrypted_message)):
        pos_encryp_msg = alphabet.index(encrypted_message[i])
        pos_key = alphabet.index(resized_key[i])

        current_pos = pos_encryp_msg - pos_key

        if current_pos < 0:
            current_pos += length_alphabet

        result.append(alphabet[current_pos])

    print(40 * '-')
    print("The original message is: {}".format(''.join(result)))


if __name__ == '__main__':
    main()
