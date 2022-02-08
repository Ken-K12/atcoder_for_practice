N = int(input())
a = list(map(int, input().split()))

Alice = 0
Bob = 0

while a:
    Alice1 = 0
    Bob1 = 0

    for i in a:
        if Alice1 < i:
            Alice1 = i
    Alice += Alice1
    a.remove(Alice1)

    if a:
        for i in a:
            if Bob1 < i:
                Bob1 = i
        Bob += Bob1
        a.remove(Bob1)



print(Alice - Bob)