# Solving

## Random number generator
The only thing from the algorithm that we can't reproduce in Python is the random number generator. We can work around that using a dummy C program:
```c
int seed = 17;
srand(seed);
for (int i = 0; i < seed; i++)
    printf("%d\n", rand());
```
Record the produced numbers to a Python list (`rands`)

## [Final solution (solver.py)](solver.py)
The `flag` and `ptr` arrays will be printed to `stdout`

## [Key formatter (key-formatter.py)](key-formatter.py)
Using the `flag` array from above, decode it to ASCII and print to `stdout`

---
## << [Previous](SOLUTION_2.md)
