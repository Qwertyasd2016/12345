import string
F = open('en-ru.txt')
S = F.read()
print(S)
S = list(map(str, S.split()))
E = []
R = []
for i in range(0, len(S), 3):
    E.append(S[i])
for i in range(2, len(S), 3):
    R.append(S[i])
D = dict(zip(E, R))
F = open('input.txt')
T = F.read()
T = T.lower()
T = list(map(str, T.split()))
for i in range (len(T)):
    for j in range(len(T[i])):
        if T[i][j] in string.punctuation:
            T[i] = T[i].replace(T[i][j], ' ')
F = open('output.txt', 'w')
for i in range(len(T)):
    if T[i] in D:
        T[i] = D[T[i]]
    F.write(T[i])
    F.write(' ')