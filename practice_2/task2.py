def get_number_sequence_of_length_n(n) -> list:
    number_sequence = []
    if n < 0 or n == 0:
        return number_sequence
    for size_of_fragment in range(1, n + 1):
        for number_in_fragment in range(size_of_fragment):
            number_sequence.append(size_of_fragment)
    return number_sequence


if __name__ == '__main__':
    number = int(input("Enter positive number "))
    sequence = get_number_sequence_of_length_n(number)
    print(*sequence[:number])
