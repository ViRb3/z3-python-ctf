from z3 import *

rands = [1227918265, 3978157, 263514239, 1969574147, 1833982879,
         488658959, 231688945, 1043863911, 1421669753, 1942003127,
         1343955001, 461983965, 602354579, 726141576, 1746455982,
         1641023978, 1153484208, 945487677, 1559964282, 1484758023]
seed = 17

s = Solver()

flag = [BitVec(f"flag_{i}", 8) for i in range(0, seed)]
ptr = [BitVec(f"ptr_{i}", 32) for i in range(0, seed)]

s.add(ptr[0] == 2 * seed + rands[0] % (5 * seed))

for i in range(1, seed):
    v5 = ptr[i-1]
    s.add(ptr[i] == v5 + rands[i] % 94 + 33)

for j in range(0, seed):
    v9 = BitVecVal(0, 32)
    for k in range(0, j+1):
        v9 += ZeroExt(24, flag[k])
    s.add(ptr[j] == v9)

print(s.check())
model = s.model()
print(model)
