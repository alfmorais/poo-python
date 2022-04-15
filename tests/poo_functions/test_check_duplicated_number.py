from src.poo_functions.set_functions import check_duplicated_number


def test_check_duplicated_number():
    main_list = [
        [1, 2, 3, 1, 4, 5, 6, 7, 9, 8],
        [1, 2, 3, 1, 4, 5, 6, 7, 9, 8],
    ]

    for list in main_list:
        response = check_duplicated_number(main_list=list)
        assert response == 1


def test_check_duplicated_number_returning_one():
    main_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    ]

    for list in main_list:
        response = check_duplicated_number(main_list=list)
        assert response == -1
