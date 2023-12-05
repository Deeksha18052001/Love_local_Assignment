def lengthOfLastWord(s):
    # Trim the trailing and leading spaces in the string
    s = s.strip()

    # Initialize the length of the last word to 0
    length = 0

    # Iterate through the string from right to left
    for i in range(len(s)-1, -1, -1):
        # If a space is encountered, break the loop and return the length of the last word
        if s[i] == ' ':
            break
        # If a non-space character is encountered, increment the length of the last word
        length += 1

    # Return the length of the last word
    return length