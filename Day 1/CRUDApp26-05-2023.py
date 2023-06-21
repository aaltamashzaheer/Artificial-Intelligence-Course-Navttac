dic = {}
print("******************************\n"
      "Welcome to the CRUD App:\n"
      "Kindly select the following options:\n"
)
def cond():
    condition = int(input("1: To add a record:\n"
              "2: To remove a record:\n"
              "3: To update a record:\n"
              "4: To access a record:\n"
              "5  To Quit: "))
    return condition

def add(name, key):
    dic[name] = key
def remove(name):
    dic.pop(name)
def update(name, key):
    dic[name] = key
def access(name):
    print(dic[name])
def qut():
    quit()
def condition1(condition):
    if condition == 1:
        name = input("Kindly Enter the Key: ")
        key = input("Enter the value of the key: ")
        add(name, key)
    elif condition == 2:
        name = input("Kindly Enter the Key: ")
        remove(name)
    elif condition == 3:
        name = input("Kindly Enter the Key: ")
        key = input("Enter the value of the key: ")
        update(name, key)
    elif condition == 4:
        name = input("Kindly Enter the Key: ")
        access(name)
    elif condition == 5:
        qut()
    else:
        print(dic)
    print(dic)

while True:
    x = cond()
    condition1(x)