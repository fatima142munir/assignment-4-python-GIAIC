
def get_first_element(lst):
    if len(lst) != 0:
        print(lst[-1])
    else:
        print("Empty list! User did'nt enter any element.")

def get_last():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_last()
    get_first_element(lst)


if __name__ == '__main__':
    main()

