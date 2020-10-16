def sieve(last):
    num = int(last) + 1
    visit = [True for i in range(num)]
    for i in range(3, num, 2):
        for j in range(i*i, num, 2*i):
            visit[j] = False
    print("Prime numbers are given below:")
    print("2", end = " ")
    for i in range(3, num, 2):
        if visit[i]:
            print(i, end = " ")
    print()


number = input("Enter a number: ")
sieve(number)