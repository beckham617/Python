#3-4
guests = []
guests.append('Pato')
guests.append('Modeste')
guests.append('Witsel')
print('Hello, '+guests[0]+'! Welcome to our dinner!')
print('Hello, '+guests[1]+'! Welcome to our dinner!')
print('Hello, '+guests[2]+'! Welcome to our dinner!\n')

#3-5
print('What a pity, '+guests[2]+' cannot be present at our dinner!')
guests[2]='Quan'
print('Hello, '+guests[0]+'! Welcome to our dinner!')
print('Hello, '+guests[1]+'! Welcome to our dinner!')
print('Hello, '+guests[2]+'! Welcome to our dinner!\n')

#3-6
print("Good news! I've found a much bigger table!")
guests.insert(0,'Sun')
guests.insert(2,'Wang')
guests.append('Zhang')
print('Hello, '+guests[0]+'! Welcome to our dinner!')
print('Hello, '+guests[1]+'! Welcome to our dinner!')
print('Hello, '+guests[2]+'! Welcome to our dinner!')
print('Hello, '+guests[3]+'! Welcome to our dinner!')
print('Hello, '+guests[4]+'! Welcome to our dinner!')
print('Hello, '+guests[5]+'! Welcome to our dinner!\n')

#3-7
print("I'm so sorry! I can't get the table right now, so I can only invite 2 guests to the dinner!")
guest_pop = guests.pop()
print("Sorry, "+guest_pop+", I don't have enough room to invite you! Welcome next time!")
guest_pop = guests.pop()
print("Sorry, "+guest_pop+", I don't have enough room to invite you! Welcome next time!")
guest_pop = guests.pop()
print("Sorry, "+guest_pop+", I don't have enough room to invite you! Welcome next time!")
guest_pop = guests.pop()
print("Sorry, "+guest_pop+", I don't have enough room to invite you! Welcome next time!")
print('Dear '+guests[0]+', you can still stay for the dinner!')
print('Dear '+guests[1]+', you can still stay for the dinner!')
del guests[1]
del guests[0]
print(guests)
#print('guests = -'+str(guests)+'-')
