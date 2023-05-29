period = int(input())
checked_patients = 0
unchecked_patients = 0
doctors = 7
for day in range(1, period+1):
    if day % 3 == 0 and unchecked_patients > checked_patients:
        doctors += 1
    patient_num = int(input())
    if patient_num <= doctors:
        checked_patients += patient_num
    elif patient_num > doctors:
        checked_patients += doctors
        unchecked_patients += abs(patient_num - doctors)

print(f"Treated patients: {checked_patients}.")
print(f"Untreated patients: {unchecked_patients}.")