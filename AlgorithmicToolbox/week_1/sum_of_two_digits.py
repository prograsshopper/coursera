def sum_of_two_digits(num1, num2):
    return num1 + num2

if __name__ == '__main__':
   nums = input().split(' ')
   print(sum_of_two_digits(int(nums[0]), int(nums[1])))