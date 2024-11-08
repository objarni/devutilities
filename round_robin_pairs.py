import random

minutes = int(input("How many minutes at your disposal: "))
switchtime = int(input("How many minutes does it take to switch room: "))
people = input("People names separated with spaces: ").split()
random.shuffle(people)
num_people = len(people)
person_list = []

for i in range(int(num_people)):
  person_list.append(people[i])

if (len(person_list) % 2) != 0:
  person_list.append('Pause')

x = person_list[0:int(len(person_list) / 2)]
y = person_list[int(len(person_list) / 2):len(person_list)]

matches = []

for i in range(len(person_list) - 1):
  rounds = {}
  if i != 0:
    x.insert(1, y.pop(0))
    y.append(x.pop())
  matches.append(rounds)
  for j in range(len(x)):
    rounds[x[j]] = y[j]

session_num = len(matches)
available_minutes = minutes - switchtime*session_num
print(
    f"Each session is limited to {available_minutes/num_people} minutes."
)
for i in range(len(matches)):
  print(f"\nSession {i+1}:")
  for (ix, (k, v)) in enumerate(matches[i].items()):
    print(f"Room {ix+1}: {k} {v}")
