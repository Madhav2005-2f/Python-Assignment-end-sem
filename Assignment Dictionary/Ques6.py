#Write a program that takes a list of strings as input and generate a dictionary with the strings as keys and frequency counts as the values. Display the returned dictionary generated.
def count_strings(strings):
    frequency_dict = {}
    for string in strings:
        if string in frequency_dict:
            frequency_dict[string] += 1
        else:
            frequency_dict[string] = 1
    return frequency_dict   