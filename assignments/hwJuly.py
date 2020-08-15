# Step 1: Initial amount = $1000
initial_amount = 1000
# Step 2: Fixed profit is assigned to .07*1000 per day
fixed_profit = initial_amount * .07
# Step 3: (Fixed profit * 7 days ) = weeklyProfit
weekly_profit = fixed_profit * 7
# Step 4: .07*1000 =70 
print(weekly_profit)
# Step 5: 70*7 =490+1000
print(weekly_profit)
# Step 6: Solution: $1490 (combining Step 1 with Step 3)
total = weekly_profit+initial_amount
print(total)