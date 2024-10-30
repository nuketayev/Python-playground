friends = [("Aka", 19),
           ("Aba", 21),
           ("Pipo", 17),
           ("Lalo", 11),
           ("Pasqiv", 33),]

age = lambda data:data[1] > 17

adult_friends = list(filter(age,friends))

for i in adult_friends:
    print(i)