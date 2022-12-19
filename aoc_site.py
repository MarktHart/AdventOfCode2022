import os
import requests
from bs4 import BeautifulSoup as bs

BASE_URL = "https://adventofcode.com"
YEAR = 2022
FOLDER = os.path.dirname(os.path.abspath(__file__))

def aoc_get(day, url=""):
    headers = {"User-Agent": f"https://github.com/MarktHart/AdventOfCode{YEAR}"}
    cookies = {"session": open(os.path.join(FOLDER, "koekje"), "r").read()}

    response = requests.get(f"{aoc_base_url(day)}{url}", headers=headers, cookies=cookies)
    response.raise_for_status()
    return response

def aoc_base_url(day):
    return f"{BASE_URL}/{YEAR}/day/{day}"

def download_input(day):
    save_dir = os.path.join(FOLDER, f"{day:02d}")
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_path = os.path.join(save_dir, "i")
    if os.path.exists(save_path):
        return

    response = aoc_get(day, "/input")
    with open(save_path, "wb") as f:
        f.write(response.content)

def download_answers(day):
    if not(content:=cache(day)):
        response = aoc_get(day)
        html = bs(response.content, "html.parser")
        content = html.body.main
    answers = [answer.contents[0] for part in content.find_all("p", recursive=False) if (answer:=part.code)]
    if len(answers) >= 2:
        save_cache(day, content)
    return answers


def cache_path(day):
    return os.path.join(FOLDER, f"{day:02d}", ".cache")

def save_cache(day, content):
    with open(cache_path(day), "w") as f:
        f.write(str(content))

def cache(day):
    path = cache_path(day)
    if not os.path.exists(path):
        return None
    return bs(open(path, "rb").read(), "html.parser").main
