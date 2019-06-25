def minimalNumberOfCoins(coins, price):
    c=0
    n=len(coins)-1
    for i in range(n,-1,-1):
        if price//coins[i]>0:
            c+=price//coins[i]
            price=price%coins[i]
    return c
        
        