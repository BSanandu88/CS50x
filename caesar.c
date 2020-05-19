#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    int key = atoi(argv[1]);
    int shift = key % 26;

    // checks for valid integer at command prompt
    if (argc != 2 || atoi(argv[1]) < 1)
        return 1;

    // requests text from user
    string input = GetString();

    // encyphers text
    int i;
    int n = strlen(input);
    for (i = 0; i < n; i++)
    {
        int ascii = input[i];
        int result = ascii + shift;
        if (ascii > 64 && ascii < 91)
        {
            if (result > 90)
            {
                printf("%c", (64 + (result - 90)));
            }
            else
            {
                printf("%c", result);
            }
        }
        else if (ascii > 96 && ascii < 123)
        {
            if (result > 122)
            {
                printf("%c", (96 +(result - 122)));
            }
            else
            {
                printf("%c", result);
            }
        }
        else
        {
            printf("%c", input[i]);
        }
    }

    printf("\n");
}