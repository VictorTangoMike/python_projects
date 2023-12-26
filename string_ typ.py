

execution_number = int(input())
result = []

for i in range(execution_number):
    number_1, number_2 = input().split(" ")

    count = 0
    for i in number_2:
        count += 1
        
    if len(number_2) > len(number_1):
        print("nao encaixa") 
    elif(number_1[-(count):] == number_2):
        print("encaixa")
    else:
        print("nao encaixa")