from src.poo_functions.set_functions import list_generator


def test_list_generator():
    main_list = list_generator()

    assert len(main_list) == 10

    for list in main_list:
        assert len(list) == 10
