from z3 import *

for input_len in range(1, 32):
    s = Solver()
    input = [BitVec(f"i_{i}", 8) for i in range(input_len)]
    output = BitVecVal(0, 64)

    for i in range(input_len):
        output += ZeroExt(64 - 8, input[i])
        output <<= 1

    s.add(output == 0x2D64A)

    if s.check() == sat:
        m = s.model()
        solution = sorted([(d, m[d]) for d in m], key=lambda x: str(x[0]))
        flag = "".join([f"{int(str(x[1]), 10):x}" for x in solution])

        # print(solution)
        print(flag)
        break
