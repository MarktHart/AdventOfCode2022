import os
from io import StringIO
from contextlib import redirect_stdout

from aoc_page import AocPage

def main():
    for day in range(1, 20):
        aoc = AocPage(day)

        # if not os.path.isdir(aoc.dir(create=False)):
        #     continue
        
        aoc.download_input()
        aoc.download_input(example=True)
        for i in [1, 2]:
            pyfile = os.path.join(aoc.dir(), f"{i}.py")
            if not os.path.exists(pyfile):
                continue

            for answer in test_answers(pyfile, aoc, example=True):
                print(f"{day:02d}/{i}.py: {answer == aoc.answer(i, example=True)}")

            for answer in test_answers(pyfile, aoc):
                print(f"{day:02d}/{i}.py: {answer == aoc.answer(i)}")


def test_answers(pyfile, aoc, example=False):
    answer_file = "i" if not example else "j"
    get_std_out = StringIO()
    code = open(pyfile).read().replace("'i'", f"'{aoc.dir()}/{answer_file}'")
    with redirect_stdout(get_std_out):
        exec(code, locals(), locals())
    return get_std_out.getvalue().split()


if __name__ == "__main__":
    main()
