F = open('input1.txt')
S = F.read()
print(S)
S = list(map(str, S.split('\n')))
for i in range(len(S)):
    S[i] = S[i].split(':')
    S[i][1] = frozenset(S[i][1].split(' '))
C = []
L = []
print(S)
for i in range(0, len(S), 3):
    C.append(S[i])
for i in range(2, len(S), 3):
    L.append(S[i])
D = dict(zip(C, L))
print(D)