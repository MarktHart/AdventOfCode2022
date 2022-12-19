import os
import requests

BASE_URL = "https://adventofcode.com"
YEAR = 2022
FOLDER = os.path.dirname(os.path.abspath(__file__))

def download_input(day):
    save_dir = os.path.join(FOLDER, f"{day:02d}")
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    save_path = os.path.join(save_dir, "i")
    if os.path.exists(save_path):
        return
    headers = {"User-Agent": f"https://github.com/MarktHart/AdventOfCode{YEAR}"}
    cookies = {"session": open(os.path.join(FOLDER, "koekje"), "r").read()}

    response = requests.get(f"{BASE_URL}/{YEAR}/day/{day}/input", headers=headers, cookies=cookies)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)

