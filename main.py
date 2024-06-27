from src.Parser import HH
from src.FileWork import WorkWithJson
from src.Vacancy import Vacancy
from src.user_interaction import UserInteraction


if __name__ == "__main__":

    print("Привет.")
    user = UserInteraction()
    keyword = input ("Какую работу ищем?")

    n = int(input("Введите номер"))
    user.get_top_n(n)

    for vacancy in user.search_vacancy(keyword):
        vac = Vacancy.new_vacancy(vacancy)
        user.vacancy_list.append(vac)

    for vacancy in user.get_vacancy_by_dectription():
        print(vacancy)
