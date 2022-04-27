import pytest


@pytest.fixture(scope="module")
def general_list():
    return list(range(10))
