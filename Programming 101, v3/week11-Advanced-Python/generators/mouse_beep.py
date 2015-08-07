from Xlib import display


def mouse_beep():
    data = display.Display().screen().root.query_pointer()._data

    while True:
        yield data["root_x"], data["root_y"]
        input()
        data = display.Display().screen().root.query_pointer()._data

    #return data["root_x"], data["root_y"]


for pos in mouse_beep():
    print(pos)
