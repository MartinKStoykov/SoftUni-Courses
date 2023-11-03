num_list = input().split()
negatives = sum(int(num) for num in num_list if int(num) < 0)
positives = sum(int(num) for num in num_list if int(num) > 0)
print(negatives)
print(positives)
if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
elif abs(negatives) < positives:
    print("The positives are stronger than the negatives")