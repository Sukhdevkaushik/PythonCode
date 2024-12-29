def maximumProfit(prices):
    point1= 0
    point2 = 1
    profit = 0
    while point2 < len(prices):
        if prices[point2] > prices[point1]:
            profit = max(profit, prices[point2] - prices[point1])
            point2 += 1
        else:                        
            point1 = point2
            point2 += 1        
    return profit
prices = [7, 6, 4, 3, 1] 
print(maximumProfit(prices))
