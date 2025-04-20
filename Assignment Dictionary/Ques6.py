#Write a program that takes a list of strings as input and generate a dictionary with the strings as keys and frequency counts as the values. Display the returned dictionary generated.
#Example: Input: ["apple", "banana", "apple", "orange", "banana",
#                "banana", "apple", "grape", "banana", "apple"]
#Output: {'apple': 4, 'banana': 4, 'orange': 1
#         'grape': 1}
#Note: The program should be case sensitive and should count the frequency of each string in the list
def count_strings(strings):
    #Create an empty dictionary to store the frequency of each string
    frequency_dict = {}
    #Iterate over each string in the input list
    for string in strings:
        #If the string is already in the dictionary, increment its count by 1
        if string in frequency_dict:
            frequency_dict[string] += 1
        else:
            #If the string is not in the dictionary, add it with a count of 1
            frequency_dict[string] = 1
    return frequency_dict   