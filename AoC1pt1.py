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
   fuelCounter += ((convert(el)//3)-2)
print(fuelCounter)