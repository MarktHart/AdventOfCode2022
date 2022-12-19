import os
from io import StringIO
from contextlib import redirect_stdout

from aoc_site import download_input, FOLDER, download_answers

def main():
    for i_day in range(1, 32):
        day = f"{i_day:02d}"
        day_folder = os.path.join(FOLDER, day)
        if day.startswith("."):
            continue
        if not os.path.isdir(day_folder):
            continue
        
        download_input(i_day)
        answers = download_answers(i_day)
        for i, answer in enumerate(answers, start=1):
            pyfile = os.path.join(day_folder, f"{i}.py")
            if not os.path.exists(pyfile):
                continue
            
            for given_answer in given_answers(pyfile, day):
                print(f"{day}/{i}.py: {given_answer == answer}")


def given_answers(pyfile, day):
    get_std_out = StringIO()
    code = open(pyfile).read().replace("'i'", f"'{day}/i'")
    with redirect_stdout(get_std_out):
        exec(code, locals(), locals())
    return get_std_out.getvalue().split()


if __name__ == "__main__":
    main()
