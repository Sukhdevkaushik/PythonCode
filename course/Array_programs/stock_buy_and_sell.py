def maximumProfit(prices):
    if len(prices) < 2:
        return prices
    maximumProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maximumProfit += prices[i] - prices[i-1]
    return maximumProfit
        

        #if prices[point2] > prices[point1]:
        #    point2 += 1
        #else:
        #    result = result + prices[point2- 1] - prices[point1]
        #    point1 = point2
        #    point2 += 1
        #    print(prices[point1])
        #    print(prices[point2])    
    return result

prices = [100, 180, 260, 310, 40, 535, 695]
print(maximumProfit(prices))