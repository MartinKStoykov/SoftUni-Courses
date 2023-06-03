lines = int(input())
opened = False
closed = False
num1 = 0
num2 = 0
last_string = ""
for line in range(lines):
    string = input()
    if string != "(" and string != ")":
        continue
    else:
        num1 += 1
        if (string == "(" and last_string == "") or (string == "(" and last_string == ")"):
            num2 += 1
            last_string = "("
        if string == ")" and last_string == "(":
            num2 += 1
            last_string = ")"
if num1 == num2:
    print("BALANCED")

else:
    print("UNBALANCED")