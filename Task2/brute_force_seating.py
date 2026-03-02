from itertools import permutations

students = ['Asha', 'Bikash', 'Nisha', 'Rohan', 'Suman']

friends = {
    'Asha':   ['Bikash'],
    'Bikash': ['Asha', 'Nisha'],
    'Nisha':  ['Bikash'],
    'Rohan':  [],
    'Suman':  ['Rohan']
}

city = {
    'Asha':'KTM', 'Bikash':'PKR', 'Nisha':'KTM',
    'Rohan':'PKR', 'Suman':'BRT'
}

def is_valid(arrangement):
    for i in range(len(arrangement) - 1):
        a, b = arrangement[i], arrangement[i+1]
        if b in friends[a]: return False
        if city[a] == city[b]: return False
    return True

count = 0
for perm in permutations(students):
    count += 1
    if is_valid(perm):
        print('Valid arrangement found: ' + str(perm))
        break

print('Total arrangements checked: ' + str(count))