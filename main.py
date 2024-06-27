from src.Parser import HH
from src.FileWork import WorkWithJson
from src.Vacancy import Vacancy
from src.user_interaction import UserInteraction


if __name__ == "__main__":

    print("Привет.")
    user = UserInteraction()
    keyword = input ("Какую работу ищем?")
    """getting user keyword"""

    n = int(input("Введите номер"))
    """getting the desired number of vacancies"""
    user.get_top_n(n)

    for vacancy in user.search_vacancy(keyword):
        vac = Vacancy.new_vacancy(vacancy)
        user.vacancy_list.append(vac)

    for vacancy in user.get_vacancy_by_dectription():
        print(vacancy)
