# Z3 Basics

## Terminology

### BitVec
- A vector of bits
- Has no initial value
- A `BitVec` of `8 bits` = `1 byte`

### BitVecVal
- A `BitVec` with initial value

### ZeroExt / SignExt
- A way to convert between different Z3 data types
- `ZeroExt` extends with `trailing` 0s
- `SignExt` extends with `leading` 0s
- `ZeroExt(24, foo)` -> extends an `8-bit` byte `foo` to a `32-bit` int

### Solver
- The theorem solver
- Constrains are added using `Solver.add(...)`

### Arithmetic logic
- When performing operations on Z3 data types, Z3 will use the `expression` rather than computing the values:
```python
foo = BitVecVal(0, 8)
bar = [BitVec(f"bar_{i}", 8) for i in range(0, 3)]
for i in range(0, 3):
    foo += bar[i]

# result actual value of foo:
# (foo + bar[0] + bar[1] + bar[2])
```

---
## << [Previous](SOLUTION_1.md) | [Next](SOLUTION_3.md) >>
