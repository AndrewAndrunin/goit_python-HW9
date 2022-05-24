from parserandhandler import parser, hello, add, change, phone, show_all, bye

#(hello, add [name] [number], change [name] [number], phone [name], show all or exit)



def main():

    dictionary = {}

    while True:
        ans = input('Print one of commands: ')
        ans2 = parser(ans)
        if ans == ".":
            break
        elif ans2[0] == 'hello':
            print(hello())
            continue
        elif ans2[0] == 'add':
            add(ans2[1], ans2[2], dictionary)
            continue
        elif ans2[0] == 'change':
            change(ans2[1], ans2[2], dictionary)
            continue
        elif ans2[0] == 'phone':
            print(phone(ans2[1], dictionary))
            continue
        elif ans2[0] == 'show_all':
            show_all(dictionary)
            continue
        elif ans2[0] == 'close' or ans2[0] == 'exit' or ans2[0] == 'good_bye':
            print(bye())
            break
   


if __name__ == '__main__':
    main()
