def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    return gcd(num2, num1%num2)

if __name__ == "__main__":
    input = input()
    num1, num2 = map(int, input.split())
    if num1 > num2:
        print(gcd(num1, num2))
    else:
        print(gcd(num2, num1))