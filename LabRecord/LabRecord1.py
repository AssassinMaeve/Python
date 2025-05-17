# Generate Prime and Fibonacci numbers within the range given by user as input.

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))

def prime(start, end):
    primeNumbers = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primeNumbers.append(i)
    return primeNumbers

def fibonacci(n):
    fibNumbers = []
    a, b = 0, 1
    while a <= n:
        fibNumbers.append(a)
        a, b = b, a + b
    return fibNumbers

primeNumbers = prime(start, end)
fibNumbers = fibonacci(end)
print("Prime numbers between", start, "and", end, "are:", primeNumbers)
print("Fibonacci numbers up to", end, "are:", fibNumbers)