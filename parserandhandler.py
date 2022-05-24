
def input_error(func):
    def inner(*args):
        result = func(*args)

        if result == 'Base_error':
            print("Bot doesn’t recognize this command, try again please ")
            return "Bot doesn’t recognize this command, try again please "
        elif result == 'Error1':
            print("Enter user name please")
            return "Enter user name please"
        elif result == 'Error2':
            print("Enter name and phone please")
            return "Enter name and phone please"
        elif result == 'Error3':
            print("Too many arguments")
            return "Too many arguments"
        elif result == 'Error4':
            print("This name is in dictionary already")
            return "This name is in dictionary already"        
        elif result == 'Error5':
            print("This name is not in dictionary")
            return "This name is not in dictionary"   
        elif result == 'Error6':
            return "This name is not in dictionary"       
        else:
            return result
        
    return inner


########
#parser
########


@input_error
def parser(str_base):
    
    str = str_base.split()

    if len(str) == 1:
        a = str[0].lower()

        if a == 'hello':
            return [a]
        elif a == 'close' or a == 'exit':
            return [a]
        elif a == 'phone':
            return 'Error1'      
        elif a == 'add':
            return 'Error2'
        elif a == 'change':
            return 'Error2'             
        elif a == '.':
            return [a]
        else:
            return 'Base_error'

    elif len(str) == 2:
        a = str[0].lower()
        b = str[1].lower()

        if a == 'show' and b == 'all':
            return ['show_all']
        elif a == 'good' and b == 'bye':
            return ['good_bye']
        elif a == 'phone':
            return ['phone', str[1]]
        elif a == 'add' or a == 'change':
            return 'Error2'
        elif a == 'hello' or a == 'close' or a == 'exit':
            return 'Error3'
        else:
            return 'Base_error'

    elif len(str) == 3:
        a = str[0].lower()

        if a == 'add':
            return ['add', str[1], str[2]]
        elif a == 'change':
            return ['change', str[1], str[2]]
        elif a == 'phone' or a == 'hello' or a == 'close' or a == 'exit' or a == 'good' or a == 'show':
            return 'Error3'
        else:
            return 'Base_error'
    
    elif len(str) > 3:
        a = str[0].lower()
        
        if a == 'phone' or a == 'add' or a == 'change' or a == 'close' or a == 'exit':
            return 'Error3'      
        else:
            return 'Base_error'           
    


########
#handler
########



def hello():
    return "How can I help you?"

@input_error
def add(name, number, dictionary):
    for k, v in dictionary.items():
        if k == name:
            return 'Error4'
    dict = {name: number}
    dictionary.update(dict)


@input_error
def change(name, number, dictionary):
    for k, v in dictionary.items():
        if k != name:
            continue
        elif k == name:
            dict = {name: number}
            dictionary.update(dict)
            return dict
    return 'Error5'

@input_error    
def phone(name, dictionary):
    for k, v in dictionary.items():
        if k == name:
            return v
    return 'Error6'

def show_all(arg):
    for k, v in arg.items():
         print(f'{k}: {v}')

def bye():
    return "Good bye!"




if __name__ == '__main__':
    while True:
      a = input('Print one of commands: ')
      if a == '.':
          break
      else:
          b = parser(a)
          #print(b)
          continue

