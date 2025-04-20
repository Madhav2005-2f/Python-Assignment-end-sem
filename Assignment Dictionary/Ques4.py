#Write a program to sort a dictionary by value in ascending or descending as per the choice of the user.
def sort_dict(d, rev=False):
    new_dict = {}
    while d:
        keys = list(d.keys())
        selected_key = keys[0]
        selected_value = d[selected_key]

        for key in keys:
            if not rev:
                if d[key] < selected_value:
                    selected_key = key
                    selected_value = d[key]
            else:
                if d[key] > selected_value:
                    selected_key = key
                    selected_value = d[key]

        new_dict[selected_key] = selected_value
        del d[selected_key]

    return new_dict

dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
print(sort_dict(dict, False))