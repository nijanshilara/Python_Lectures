##Q4. [Functions] Write a function apply_discount(prices, percent) that reduces every price in the given list by the given percentage IN PLACE (modifying the original list). Print the list before and after the call.

def apply_discount(prices, percent):
    for i in range(len(prices)):
        prices[i] = prices[i] - (prices[i] * percent / 100)

prices = [100, 200, 300, 400]

print("Original:", prices)
apply_discount(prices, 10)
print("After discount:", prices)