s_range= int(input("Enter the start range: "))
e_range= int(input("Enter the end range: "))
for n in range(s_num, e_num+1 ):
    if n> 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
