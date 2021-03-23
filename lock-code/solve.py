from z3 import *

s = Solver()
code = IntVector("x", 3)


def GoodValueBadPlace(nums, count):
    exps = []
    for i in range(len(nums)):
        for j in range(len(code)):
            if i == j:
                continue
            else:
                exps.append(If(nums[i] == code[j], 1, 0))
    return Sum(exps) == count


# one number is correct and well placed
s.add(Or(code[0] == 2, code[1] == 9, code[2] == 1))
# one number is correct but wrong placed
s.add(GoodValueBadPlace([2, 4, 5], 1))
# two numbers are correct but wrong placed
s.add(GoodValueBadPlace([4, 6, 3], 2))
# nothing is correct
s.add(And(code[0] != 5, code[1] != 7, code[2] != 9))
# one number is correct but wrong placed
s.add(GoodValueBadPlace([5, 6, 9], 1))

while s.check():
    m = s.model()
    print(m[code[0]], m[code[1]], m[code[2]])
    s.add(Or([m[code[i]] != code[i] for i in range(3)]))
