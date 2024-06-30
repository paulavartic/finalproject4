class Vacancy:
    def __init__(self, name: str, url: str, salary: int | None, snippet: str | None):
        self.name: str = name
        self.url: str = url
        self.salary: int = self.__data_validation(salary)
        self.snippet: str | None = snippet

    @staticmethod
    def __data_validation(salary: int | None) -> int:
        return salary or 0

    def __lt__(self, other):
        if not self.salary:
            return "Не указано"
        elif not other.salary:
            return "Не указано"
        elif self.salary < other.salary:
            return True
        else:
            return False

    def __str__(self):
        return (f"Вакансия: {self.name}\n"
                f"Ссылка: {self.url}\n"
                f"Зарплата от:{self.salary if self.salary else 'Не указано'}\n"
                f"Требования: {self.snippet}")

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        url = vacancy.get("url")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = vacancy.get("salary").get("from")
            else:
                salary = 0
        else:
            salary = 0
        snippet = vacancy.get("snippet").get("requirement")
        return cls(name, url, salary, snippet)
