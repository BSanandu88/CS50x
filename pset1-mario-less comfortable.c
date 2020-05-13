#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get and validate user input
    int user_input;
    do
    {
        user_input = get_int("Height: ");
    }
    while (user_input < 1 || user_input > 8);

    // Row loop
    for (int row = 1; row <= user_input; row++)
    {
        // Column loop - spaces
        for (int spaces = user_input - row; spaces > 0; spaces--)
        {
            printf(" ");
        }

        // Column loop - left hand hashes
        for (int hashes = 1; hashes <= row; hashes++)
        {
            printf("#");
        }

        // Spaces between the hashes
        printf("  ");

        // Column loop - right hand hashes
        for (int hashes = 1; hashes <= row; hashes++)
        {
            printf("#");
        }

        // New row
        printf("\n");
    }
}
