def get_dictionary_from_lists(number_list, character_list) -> dict:
    dictionary = {}
    for index_of_number in range(len(number_list)):
        current_character = character_list[index_of_number]
        if current_character not in dictionary:
            dictionary[current_character] = 0
        dictionary[current_character] += number_list[index_of_number]
    return dictionary


if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    list_b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    print(get_dictionary_from_lists(list_a, list_b))
