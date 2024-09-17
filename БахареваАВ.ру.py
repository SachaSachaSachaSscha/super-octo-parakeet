import math

def task1(a,b,c,d):  
    d = d*8
    i = 2**(d/(a*b*c))
    return int(i)

def task2(a, b):
    i = (math.log2(a))/(math.log2(b)) 
    return i

def task3(N, soo):
    K = soo/math.log2(N)
    return int(K)

def task4(where):
    i = 2**int(where)
    return i

def task5(blue,bit):
    i = (blue*blue) / (2**bit)
    return int(i)

if __name__ == "__main__":
    #inp1 = int (input("количество страничек: "))  #task1 №18
    #inp2 = int (input("количество строчек: "))
    #inp3 = int (input("количество символов: "))
    #inp4 = int (input("количество битов: "))
    #print(task1(inp1, inp2, inp3, inp4))

    #inp5 = int(input("мощность 1 алфавита: "))    #task2 №19
    #inp6 = int(input("мощность 2 алфавита: "))
    #print(task2(inp5, inp6))

    #inp7 = int(input("количество букв в алфавите: "))    #task3 №20
    #inp8 = int(input("количество бит в сообщении: "))
    #print(task3(inp7, inp8))

    #inp9 = int(input("количество бит в сообщении : "))    #task4 
    #print(task4(inp9))

    inp10 = int(input("количество потраченной синей краски: "))   #task4 №7
    inp11 = int(input("количество бит: "))
    print(task5(inp10,inp11))