

list_of_lists = [['a', 'b', 'c'], [0, 1, 2]]
list_of_lists2 = [['a', 'list', 'of', 'words'],
                  [1, 5, 209], [True, True, False]]
confusing_list = [[23, 73, 50], 'some words',
                  12.308, [[False, True], 'more words']]
grocery_list = ['chicken', 'onions', 'rice', 'peppers', 'bananas']
example_list = [1, 2, 3]

def main():
    print(list_of_lists)
    print(list_of_lists2)
    print(confusing_list)
    print('2nd element in confusing_list')
    print(confusing_list[1])

    print('All elements of groceries')
    print(grocery_list)
    print('last 3 elements in')
    print(grocery_list[-3:])
    print('last 2nd elements in')
    print(grocery_list[-2])
    print('Elements from 1 upto 4 not including 4')
    print(grocery_list[1:4])
    print('Elements after 3 ')
    print(grocery_list[3:])
    print('Elements before 3 including 3rd element')
    print(grocery_list[:3])
    print('select every other element starting with the very first element')
    print(grocery_list[::2])
    print('Select every other element starting with the second element.')
    print(grocery_list[1::2])
    print('Reverse and elements 4 to 1')
    print(grocery_list[4:1:-1])
    print("Range from 0 to last element step size of 2")
    for i in range(0, len(grocery_list), 2):
        print(i, grocery_list[i])

    print("Range from 0 to 10 with gap 3")
    print(list(range(0, 10, 3)))
    print("Range from 104 to 100 in a negative way")
    print(list(range(104, 100, -1)))
    print(list(range(5)))  # starts at 0 and counts by 1 by default

    # difference of append and extend
    print("append squash")
    grocery_list.append('squash')
    print(grocery_list)
    print("append ['bread', 'salt']")
    grocery_list.append(['bread', 'salt'])
    print(grocery_list)

    print("Delete last 2 item")
    del grocery_list[-1]        # delete the last item
    print(grocery_list)
    print("extend ['bread', 'salt']")
    grocery_list.extend(['bread', 'salt'])
    print(grocery_list)

    # remove the last item from the list and return it
    print("Pop and print last element")
    print(grocery_list.pop(-1))
    print("After Pop, print whole list again")
    print(grocery_list)

    print("After sorting")
    grocery_list.sort()
    print(grocery_list)
    dir(grocery_list)

    print("Print upacked list")
    a, b, c = example_list
    print(a)
    print(b)
    print(c)

if __name__ == "__main__":
    main()
