import script01 as s1

def getInput():
    name = input ('enter yur name: ')

def function_01():
    print("I am in Script 02 - inside function_01")


def function_02():
    print("I am in Script 02 - inside function_02")

if __name__ == '__main__':
    getInput()
    function_01()
    s1.function_02()

# print(f'in script 02 : {__name__}')
