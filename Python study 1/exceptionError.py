#This program test for try and exception
valuentered = [0, 'r', 10, 5]

for entry in valuentered:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print(f'The reciprocal of {entry}, is, {r}')
