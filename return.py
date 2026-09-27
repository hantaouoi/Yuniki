y = int(input())
x = int(input())
def add(x,y):
    z = x + y
    return z
print (add(y, x))


def create_name(first , last):
    last = last.capitalize ()
    first = first.capitalize ()
    return first + " " + last
full_name = create_name("Kol", "Code")
print (full_name)