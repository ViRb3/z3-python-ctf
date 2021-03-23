# Analysis

## Decompiling
We land in the `main` method, which is also the only place we are interested in. Decompile it (requires [IDA Pro](https://www.hex-rays.com/products/ida/index.shtml)):
- Hide casts (hotkey: `\`)
- Create new struct type for `ptr`

We end up with [sonda.c](sonda.c)

## Understanding the algorithm
```c
printf("Give me the magic number: ", argv, envp);
__isoc99_scanf("%d", &seed);
if ( seed % 17 || seed > 20 )
{
    puts("BAD...");
    result = 1;
}
```
The only valid numbers that don't produce a remainder are `0` and `17`

```c
s = malloc(seed);
printf("Tell me more: ");
__isoc99_scanf("%s", s);
v4 = strlen(s);
if ( v4 <= seed )
{
    /* ... */
}
else
{
    puts("WTF is wrong with u?");
    free(s);
    result = 1;
}
```

`s` is our flag. We see that it must be the same length as the value of `seed`. Since a flag with length `0` doesn't make sense, we deduce that seed _must_ be `17`, and so must be the length of the flag


```c
srand(seed);
```

This seeds the random number generator. Since the seed is always `17`, the produced random numbers will be identical between runs, but still different for each call during the same run

```c
ptr = malloc(4LL * seed);
*ptr = 2 * seed + rand() % (5 * seed);
for ( i = 1; i < seed; ++i )
{
    v5 = ptr[i - 1];
    ptr[i] = v5 + rand() % 94 + 33;
}
```

`ptr` is initialized as an array of `4 byte` ints. All elements are filled based on the seed and the produced random numbers

```c
for ( j = 0; j < seed; ++j )
{
    v9 = 0;
    for ( k = 0; k <= j; ++k )
        v9 += s[k];
    if ( v9 != ptr[j] )
    {
        puts("NOOB! Keep trying...");
        free(s);
        free(ptr);
        return 1;
    }
}
```

For each character of the flag, `v9` (`4 byte` int) is calculated:  
- the values of all characters before and including the current character are added together

`v9` must be equal to the number at the same position in `ptr`

---
## [Next](SOLUTION_2.md) >>
