import sys
def last_digit_fibo(num):
    prev = 0
    curr = 1
    
    if num <= 1:
        return num
    
    for _ in range(0, num-1):
        prev, curr = curr, (prev + curr) % 10
    return curr

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(last_digit_fibo(n))