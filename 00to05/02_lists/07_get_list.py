
def get_first_element(list_1):
    if len(list_1) != 0:
        print("User List is here:")
        for i in range(len(list_1)):
            print(list_1[i])
    else:
        print("Empty list! User did'nt enter any element.")

def get_list():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_list()
    get_first_element(lst)


if __name__ == '__main__':
    main()

