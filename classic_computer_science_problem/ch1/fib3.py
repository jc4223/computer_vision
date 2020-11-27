memo = {0:0, 1:1}

def fib3(n: int) ->int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]



if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))