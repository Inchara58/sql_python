def dp(n, memo={}):
    
    if n in memo:
        return memo[n]
    
   
    if n <= 1:
        return n

    memo[n] = dp(n - 1, memo) + dp(n - 2, memo)
    return memo[n]



if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = dp(n)
    print(f"Fibonacci of {n} is: {result}")