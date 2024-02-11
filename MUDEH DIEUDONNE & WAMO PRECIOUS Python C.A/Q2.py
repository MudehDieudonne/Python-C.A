def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiou"
    s = s.lower()
    count = sum(1 for char in s if char in vowels)
    return count

s = "Good Morning"
count = count_vowels(s)
print(f"The number of vowels in '{s}' is {count}.")