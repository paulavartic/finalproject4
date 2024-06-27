import pytest

from src.user_interaction import UserInteraction
from src.Vacancy import Vacancy


@pytest.fixture
def test():
    test = UserInteraction()
    test_list = [Vacancy(f"testname{i}", f"testurl{i}", i * 1000, f"testsnippet{i}") for i in range(10)]
    test.vacancy_list = test_list
    return test


def test_get_top_n(test):
    assert UserInteraction.get_top_n(test, 0) == []


def test_get_top_n_1(test):
    assert len(UserInteraction.get_top_n(test, 5)) == 5


def test_get_top_n_2(test):
    assert UserInteraction.get_top_n(test, 1)[0].salary == 9000




