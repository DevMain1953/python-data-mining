def get_second_powers_of_numbers() -> list:
    second_powers = []
    first_number = int(input("Enter the first number "))
    next_number = int(input("Enter the next number "))
    final_sum = first_number + next_number
    second_powers.append(first_number ** 2)
    second_powers.append(next_number ** 2)
    while final_sum != 0:
        next_number = int(input("Enter the next number "))
        final_sum = final_sum + next_number
        second_powers.append(next_number ** 2)
    return sum(second_powers)


if __name__ == '__main__':
    print(get_second_powers_of_numbers())
