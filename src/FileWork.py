from abc import ABC, abstractmethod
import json
import os


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self, data):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class WorkWithJson(FileWork):
    def __init__(self):
        self.file_name = ""
        self.abs_path = os.path.abspath("../finalproject4/data/vacancies.json")

    def read_file(self):
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data):
        with open(self.abs_path, "w", encoding='utf-8') as file:
            res = json.load(file)
            res.append(data)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_file(self):
        pass
