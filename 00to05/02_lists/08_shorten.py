MAX_LENGTH : int =4

def shorten(my_lst):
    while len(my_lst) > MAX_LENGTH:
        last_elem = my_lst.pop()
        print(f"Max length of list is {MAX_LENGTH} so this item {last_elem} not allowed.")


def get_list():

    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_list()
    shorten(lst)


if __name__ == '__main__':
    main()