def age_assignment(*args, **kwargs):
    final_age_data = []
    for letter, age in kwargs.items():
        for name in args:
            if name[0] == letter:
                final_age_data.append(f"{name} is {age} years old.")

    return "\n".join(sorted(final_age_data))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))