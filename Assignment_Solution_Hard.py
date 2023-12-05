def countDigitOne(n):
    # Base case: If n is less than or equal to 0, return 0
    if n <= 0:
        return 0

    # Initialize variables q, x, and ans
    q, x, ans = n, 1, 0

    # Iterate through each digit of the number n
    while q > 0:
        # Calculate the remainder and divide n by 10
        digit = q % 10
        q //= 10

        # Update the count of digit 1 based on the position and its value
        ans += q * x
        if digit == 1:
            ans += n % x + 1
        if digit > 1:
            ans += x
        x *= 10

    # Return the total count of digit 1
    return ans