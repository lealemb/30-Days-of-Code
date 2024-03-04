# First we have to take the input of the number of Strings 
NumberOfStrings = int(input().strip())
# for loop from 0 to the length of the String
for _ in range(NumberOfStrings):
    # Read the input string for this test case
    s = input().strip()

    # Separate even and odd indexed characters
    even_chars = s[::2]  # Select characters at even indices (0, 2, 4, ...)
    odd_chars = s[1::2]  # Select characters at odd indices (1, 3, 5, ...)
    print(even_chars, odd_chars)
