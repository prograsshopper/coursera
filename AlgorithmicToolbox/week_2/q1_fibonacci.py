def fibonacci(num):
    fibo_dic = dict()
    
    for i in range(0, num+1):
        fibo_dic[i] = i if i <= 1 else (fibo_dic[i-1] + fibo_dic[i-2])
    return fibo_dic[num]

num = int(input())
print(fibonacci(num))