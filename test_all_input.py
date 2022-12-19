import os
from new import download_input, FOLDER

def main():
    for day in os.listdir(FOLDER):
        day_folder = os.path.join(FOLDER, day)
        if day.startswith("."):
            continue

        if os.path.isdir(day_folder):
            download_input(int(day))

if __name__ == "__main__":
    main()
