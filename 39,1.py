def maximumwelth(accounts):
    max_wealth = 0
    for rows in accounts:
        wealth = 0
        
        for value in rows:
            wealth = wealth + value
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth

print(maximumwelth([[1,2,3],[3,2,1],[1,9,10]]))