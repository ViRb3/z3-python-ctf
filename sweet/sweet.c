int main() {
    char input[32];
    puts("Input password:");
    fgets(input, 32, stdin);

    long long sum = 0;
    for (int i = 0; i < strlen(input); i++) {
        char c = input[i];
        sum += (int)c;
        sum <<= 1;
    }

    if (sum != 0x2d64a) {
        puts("Bad password!");
    } else {
        puts("Well done!");
    }

    return 0;
}