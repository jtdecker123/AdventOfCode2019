board = []
while True:
   line = input()
   if line:
       board.append(list(line))
   else:
       break
fuelCounter = 0
def convert(list):
   s = [str(i) for i in list]
   res = int("".join(s))
   return(res)
global lst
lst = []
for el in board:
    lst.append(convert(el))
    while True:
        pop = lst.pop(0)
        if ((pop//3)-2) >= 1: 
            fuelCounter += ((pop//3)-2)
            lst.append(((pop//3)-2))
        elif ((pop//3)-2) < 1:
            break
print(fuelCounter)