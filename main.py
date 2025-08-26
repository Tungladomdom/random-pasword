import random

# Tạo chương trình chọn Pasword ngẫu nhiên #

char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Z"]
num = ["0","1","2","3","4","5","6","7","8","9"]
sym = ["!","@","#","$","%","^","&","*","(",")","_","+","=","-","{","}","[","]","|","\\",":",";","<",">",","]
passcode = []
pasword = ""

n_char = int(input("Nhập số lượng kí tự: \n"))
n_num = int(input("Nhập số lượng số: \n"))
n_sym = int(input("Nhập số lượng kí tự đặc biệt: \n"))

for i in range (0,n_char):
    passcode.append(random.choice(char))

for i in range (0,n_num):
    passcode += random.choice(num)

for i in range (0,n_sym):
    passcode += random.choice(sym)

random.shuffle(passcode)
for i in passcode:
    pasword += i

print (pasword)