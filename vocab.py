import webbrowser
import time

vocab = []
vocab8 = []
alreadyU7 = 0
alreadyU8 = 0
cont = True

def define(name, value):
  if (name + str(id(name))) not in globals():
    globals()[name + str(id(name))] = value

def constant(name):
  return globals()[name + str(id(name))]

once = input("Please enter the number of tabs you want to display once (Default: 10): ")
if once == "":
    once = 10
try:
    int(once)
except:
    print("Invalid input")
    once = input("Please enter the number of tabs you want to display once (Default: 10): ")
    
once = int(once)

define("ADD",once)


with open("U7.txt","r") as f:
    for line in f:
        vocab.append(line[0:-1])

with open("U8.txt","r") as file:
    for line in file:
        vocab8.append(line[0:-1])
        
while alreadyU7 <= 89 and cont == True:
    try:
        webbrowser.open("https://dictionary.cambridge.org/dictionary/english-chinese-traditional/" + vocab[alreadyU7])
        time.sleep(1)
        alreadyU7 = alreadyU7 + 1
        if alreadyU7 == once:
            cont = False
            askCont = input("Type \"c\" when ready to continue: ")
            if askCont == "c" or askCont == "C":
                cont = True
                once = once + constant("ADD")
    except IndexError:
        cont = True
        print("U7 finished.")
        u8Cont = input("Type \"u\" to continue display U8: ")
        once = constant("ADD")
        if u8Cont == "u" or u8Cont == "U":
            break


while alreadyU8 <= 69 and cont == True:
    try:
        webbrowser.open("https://dictionary.cambridge.org/dictionary/english-chinese-traditional/" + vocab8[alreadyU8])
        time.sleep(1)
        alreadyU8 = alreadyU8 + 1
        if alreadyU8 == once:
            cont = False
            askCont = input("Type \"c\" when ready to continue: ")
            if askCont == "c" or askCont == "C":
                cont = True
                once = once + constant("ADD")
    except IndexError:
        cont = True
        break