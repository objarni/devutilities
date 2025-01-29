jsonstring = open('event.txt').read()
cut = jsonstring.partition('"Event"')[2]
lines = cut.splitlines()
print('\n'.join(lines[:25]))


