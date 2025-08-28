# Prints all letters except 'e' and 's'
i = 0
a = 'students'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1   # move to next character before continue
        continue
    print(a[i])
    i += 1