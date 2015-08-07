import glob, os
os.chdir("/home/petar-ivanov/HackBulgaria/Programming 101, v3/week11-Advanced-Python/Book")


def book_reader():

    content = ""

    for curr_file in glob.glob("*.txt"):

        with open(curr_file, "r") as myfile:
            for curr_line in myfile:

                if '#' in curr_line:
                    yield content
                    input()
                    content = ""
                    content += curr_line
                else:
                    content += curr_line

book = book_reader()
for x in book:
    print(x)
