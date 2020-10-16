def showOdds(last):
    n = int(last) + 1
    print("All odd numbers are given below:")
    sumOfOdds = 0
    for i in range(1, n, 2):
        print(i, end = " ")
        sumOfOdds += i
    print()
    return sumOfOdds


value = input("Enter a number: ")
result = showOdds(value)
print("Sum of the following numbers: " + str(result))