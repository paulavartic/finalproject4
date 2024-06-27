from typing import List, Any

from src.Parser import HH


class UserInteraction:
    def __init__(self):
        self.vacancy_list = []

    @staticmethod
    def search_vacancy(keyword):
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_top_n(self, n):
        sort_by_salary = list(sorted(self.vacancy_list, key=lambda x: x.salary, reverse=True))
        return sort_by_salary[:n]

    def get_vacancy_by_description(self):
        keyword = input("Введите слово")
        res = []
        for vacancy in self.vacancy_list:
            if vacancy.name.find(keyword) != -1:
                res.append(vacancy)

        return res
