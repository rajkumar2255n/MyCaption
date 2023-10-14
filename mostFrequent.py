def most_frequent(input_string):
    # Create an empty dictionary to store character frequencies
    char_frequency = {}

    # Count the frequency of each character in the input string
    for char in input_string:
        if char.isalpha():
            char = char.lower()  # Convert to lowercase for case-insensitivity
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    # Sort the dictionary by value in descending order
    sorted_frequency = sorted(char_frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the characters and their frequencies
    for char, freq in sorted_frequency:
        print(f"{char} = {freq:02d}")

# Example usage
input_string = input("Enter a String:")
most_frequent(input_string)
