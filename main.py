import os, time
import pyscreenshot as ImageGrab
from Xlib import display


def move_left():
    os.system("xte 'key Left'")


def move_right():
    os.system("xte 'key Right'")


def exist_branch(x, y):
    box = (x, y - 6 * 100, x + 10, y)  # разрешение экрна
    # было x + 1 заменил на x + 10
    im = ImageGrab.grab(box)

    rgb_im = im.convert('RGB')
    rgb_im.save("scrin1.png")
    x, y = im.size

    result = []
    for i in range(0, 6):
        r, g, b = rgb_im.getpixel((0, y - 1 - i * 100)) # разбивает скриншот на 6 частей и возращает пиксель в точке по RGB
        print("---------")
        print(r)
        print(g)
        print(b)
        summa = r + g + b
        if summa < 700:
            result.append(True)
        else:
            result.append(False)
    return result


def get_mouse():
    while True:
        data = display.Display().screen().root.query_pointer()._data
        x = data["root_x"]
        y = data["root_y"]
        print('%s,%s - %s' % (str(x), str(y), exist_branch(x, y)))


def main():
    start_x = 1543
    start_y = 641

    while True:
        branches = exist_branch(start_x, start_y)

        cons_str = ""
        for elem in branches:
            if elem:
                cons_str += 'Left  '
            else:
                cons_str += 'Right '
        print(cons_str)

        for elem in branches:
            if elem:
                move_left()
                time.sleep(0.03)
                move_left()

            else:
                move_right()
                time.sleep(0.03)
                move_right()
        time.sleep(0.2)


try:

    # get_mouse()
    main()
except:
    print('Exit..')
