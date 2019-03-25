from Sort.sort import *
from pylab import *
from matplotlib import pyplot


def list_generator(inputs):
    lists = []
    for x in inputs:
        lists.append(generator(x))
    return lists


def comparison(lists, functions):
    times = []
    for i in range(6):
        temp = []
        for x in lists:
            start = time.time()
            eval(functions[i] + "(" + str(x) + ")")
            end = time.time()
            listtime = end-start
            temp.append(listtime)
        times.append(temp)
    return times

start = time.time()
inputs = [10, 100, 1000]
lists = list_generator(inputs)
functions = ["bubble_sort", "selection_sort", "insertion_sort", "heap_sort", "merge_sort", "quick_sort"]
times = comparison(lists, functions)
print(times)
end = time.time()
print(str(end-start))

plot(inputs, times[0], "b")
plot(inputs, times[1],"g")
plot(inputs,times[2],"r")
plot(inputs,times[3],"y")
plot(inputs,times[])
show()
