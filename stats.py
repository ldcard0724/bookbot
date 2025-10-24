def count_words(booktext):
    count = 0
    booktext = booktext.split()
    for words in booktext:
        count += 1
    
    return count

def count_characters(booktext):
    output_dict = {}
    for char in booktext:
        if char.lower() in output_dict:
            output_dict[char.lower()] += 1
        else:
            output_dict[char.lower()] = 1

    return output_dict

def sort_on(items):
    return items["num"]

def sort_dict(input_dict):
    list_of_dicts = []
    for item in input_dict:
        if item.isalpha():
            list_of_dicts.append({"char":item, "num":input_dict[item]})
        else:
            continue
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts