import os
import time
import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://adventofcode.com"
YEAR = 2022
FOLDER = os.path.dirname(os.path.abspath(__file__))

class AocPage:
    def __init__(self, day):
        self.day = f"{day:02d}"

    def aoc_get(self, url=""):
        print("HTTP request to AoC")
        headers = {"User-Agent": f"https://github.com/MarktHart/AdventOfCode{YEAR}"}
        cookies = {"session": open(os.path.join(FOLDER, "koekje"), "r").read()}

        response = requests.get(f"{self.aoc_base_url()}{url}", headers=headers, cookies=cookies)
        response.raise_for_status()
        return response.content

    def aoc_base_url(self):
        return f"{BASE_URL}/{YEAR}/day/{int(self.day)}"

    def download_input(self, example=False):
        filename = "j" if example else "i"
        save_path = os.path.join(self.dir(), filename)
        if os.path.exists(save_path):
            return open(save_path, "r").read()

        if example:
            article = self.article(1)
            assert "example" in str(article).lower()
            previous = None
            for part in article.find_all(True, recursive=False):
                if part.name == "pre" and "example" in str(previous).lower():
                    with open(save_path, "w") as f:
                        f.write(part.text)
                    return part.text
            assert False
        else:
            response = self.aoc_get("/input")
            with open(save_path, "wb") as f:
                f.write(response)
            return open(save_path, "r").read()

    def dir(self, create=True):
        result = os.path.join(FOLDER, self.day)
        if create and not os.path.exists(result):
            os.mkdir(result)
        return result

    def path(self, cat, i):
        return os.path.join(self.dir(), f".cache.{cat}.{i}")

    def answer(self, i, example=False):
        if example:
            article = self.article(i)
            last = None

            for par in article.find_all("p", recursive=False):
                for part in par.find_all(["code", "em"], recursive=False):
                    last = part.em or part.code or last
            if not last:
                for lst in article.find_all("ul", recursive=False):
                    example_input = self.download_input(example=True)
                    for row in lst.find_all("li", recursive=False):
                        for part in row.find_all("code", recursive=False):
                            if part.text in example_input:
                                for answer in row.find_all("em", recursive=True):
                                    return answer.text
            assert last
            return last.text
        else:
            path = self.path("answer", i)
            if not os.path.exists(path):
                self.parse()
                assert os.path.exists(path), path
            return open(path, "r").read()

    def article(self, i):
        path = self.path("article", i)
        if not os.path.exists(path):
            self.parse()
            assert os.path.exists(path), path
        return bs(open(path, "rb").read(), features="lxml").article

    def parse(self):
        html = bs(self.aoc_get(), "html.parser")
        content = html.body.main
        result = {
            "article": [
                part for part in content.find_all("article", recursive=False)
            ],
            "answer": [
                answer.contents[0] for part in content.find_all("p", recursive=False) if (answer:=part.code)
            ]
        }
        for k, vs in result.items():
            for i, v in enumerate(vs, start=1):
                with open(self.path(k, i), "w") as f:
                    f.write(str(v))

