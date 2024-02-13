electrons = int(input())
shell_list = []
def shell_formula(num):
    return 2 * num ** 2
shell = 1
while electrons > 0:
    if electrons >= shell_formula(shell):
        electrons -= shell_formula(shell)
        shell_list.append(shell_formula(shell))
        shell += 1
    else:
        shell_list.append(electrons)
        break
print(shell_list)