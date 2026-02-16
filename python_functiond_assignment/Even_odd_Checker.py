def even_or_odd(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

num = int(input("Enter a number: "))
res = even_or_odd(num)
print(res)
