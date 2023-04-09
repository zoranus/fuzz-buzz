
def fizzbuzz(number):
    string, value = "", ""
    for i in range(1, number + 1):
        if i % 15 == 0:
            value += "FyCS Race"
        elif i % 3 == 0:
            value += "FyCS"
        elif i % 5 == 0:
            value += "Race"
        else:
            value += str(i)
        string += value + ", "
        value = ""
    return string


while True:
    try:
        numb = int(input("enter number: "))
    except ValueError:
        continue
    else:
        if not numb > 0:
            continue
    print(fizzbuzz(numb))
