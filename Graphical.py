from matplotlib import pyplot
from matplotlib import animation
from Sort.sort import *
from collections.abc import Iterable


list = generator(25)
bubble_sort(list)
gen = list

fig, ax = pyplot.subplots()
ax.set_title("Bubble Sort")

rects = ax.bar(range(25), list, align="edge")
ax.set_xlim(0,25)
ax.set_ylim(0, 27)
loop = [0]
if isinstance(list,Iterable):
    print("True")


def update_figure(list, rects, loop):
    for rect, value in zip(rects, list):
        rect.set_height(value)
    loop[0] += 1


anim = animation.FuncAnimation(fig, func=update_figure, fargs=(rects, loop), frames=gen, interval=1, repeat=False)
pyplot.show()