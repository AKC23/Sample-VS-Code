# A Python tuple is very similar to a list with one major difference -- it is immutable.
# We create a tuple using parentheses ().
# While we can retrieve data through indexing (because a tuple is ordered),
# we cannot modify it (because a tuple is immutable).

# Both the Python `list` and `tuple` are ordered and heterogeneous. 
# However, unlike the `list`, the `tuple` is immutable, meaning it cannot be modified after it is created. 
# Therefore, a `list` might be better for representing data that is expected to change over the course of a program, 
# like a to-do list. A `tuple` might be better for representing data that is expected to be fixed, 
# like the responses of an individual subject to a survey.

# One common mistake people make with immutability and especially with tuples is to assume data structures 
# inside the tuple are immutable because the tuple is immutable.  Lets see an example.






def first_last(s):
    return s[0], s[-1]


def main():

    example_tuple = ('Dylan', 26, 167.6, True)
    print("Print tuple")
    print(example_tuple)
    # example_tuple[2] = 169.3      #cant change the value in tuple
    # print(example_tuple)

    print("Print last 2 characters of hello! ")
    chars = first_last('hello!')
    print(chars)

    # In such cases, we'll sometimes want to store the multiple outputs in separate variables.
    print("Print last 2 characters of 'hello!' with two variables ")
    first_char, last_char = first_last('hello!')
    print(first_char)
    print(last_char)

    # Unpacking tuple
    print("Print upacked tuple")
    name, age, height, has_dog = example_tuple
    print(name)
    print(age)
    print(height)
    print(has_dog)

    print("List in a tuple and change the contents")
    tup = (123, 'a')
    print(tup)
    tup = (456, 'a')            #Reassign tuple to change the contents
    # tup[0].append(1)
    print(tup)


if __name__ == "__main__":
    main()
