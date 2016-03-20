from random import randint


def generate_word():
    letters_counter = randint(0, 20)
    word = "x" * letters_counter

    return word


def book_generator(chapter_num, word_interval):
    content = ""
    for curr_chap in range(0, chapter_num):
        content += "#Chapter "+str(curr_chap)
        content += "\n\n"
        num_words = randint(word_interval[0], word_interval[1])
        for i in range(0, num_words):
            content += generate_word()
            content += " "
        content += "\n\n"
        yield content
        content = ""

generator = book_generator(8, (10, 255))

for x in generator:
    with open("bookche.txt", "a") as myfile:
                    myfile.write(x)
