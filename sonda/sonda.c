int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  size_t v4; // rax
  int v5; // ebx
  unsigned int seed; // [rsp+4h] [rbp-3Ch]
  int i; // [rsp+8h] [rbp-38h]
  int j; // [rsp+Ch] [rbp-34h]
  int v9; // [rsp+10h] [rbp-30h]
  int k; // [rsp+14h] [rbp-2Ch]
  char *s; // [rsp+18h] [rbp-28h]
  _DWORD *ptr; // [rsp+20h] [rbp-20h]
  unsigned __int64 v13; // [rsp+28h] [rbp-18h]

  v13 = __readfsqword(0x28u);
  printf("Give me the magic number: ", argv, envp);
  __isoc99_scanf("%d", &seed);
  if ( seed % 17 || seed > 20 )
  {
    puts("BAD...");
    result = 1;
  }
  else
  {
    s = malloc(seed);
    printf("Tell me more: ");
    __isoc99_scanf("%s", s);
    v4 = strlen(s);
    if ( v4 <= seed )
    {
      srand(seed);
      ptr = malloc(4LL * seed);
      *ptr = 2 * seed + rand() % (5 * seed);
      for ( i = 1; i < seed; ++i )
      {
        v5 = ptr[i - 1];
        ptr[i] = v5 + rand() % 94 + 33;
      }
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
      printf("flag{%s}\n", s);
      free(s);
      result = 0;
    }
    else
    {
      puts("WTF is wrong with u?");
      free(s);
      result = 1;
    }
  }
  return result;
}