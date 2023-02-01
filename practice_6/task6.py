from scipy.stats import chisquare as perform_one_way_chi_square_test


if __name__ == '__main__':
    expected_dice_tosses = [100, 100, 100, 100, 100, 100]
    obtained_dice_tosses = [97, 98, 109, 95, 97, 104]
    print("Checking dice tosses using chi square test: ", perform_one_way_chi_square_test(f_exp=expected_dice_tosses,
                                                                                          f_obs=obtained_dice_tosses))
