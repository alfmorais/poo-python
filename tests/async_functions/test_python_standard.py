from unittest.mock import patch

from src.async_functions.python_standard import main


@patch('src.async_functions.python_standard.to_compute')
def test_main(mock_to_compute):
    main()

    mock_to_compute.assert_called_once()
    mock_to_compute.assert_called_once_with(ends=50_000_000)
