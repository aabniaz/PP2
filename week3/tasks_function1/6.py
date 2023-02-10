def myfunc(string):
    string = string.split()
    string.sort(reverse = True)
    for i in string:
        print(i, end = " ")
myfunc(input())
