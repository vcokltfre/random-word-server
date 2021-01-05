from requests import get
from pathlib import Path

Path("./data").mkdir(exist_ok=True)

if not Path("./data/words.txt").exists():
    print("Downloading initial word list. This will only happen once.")
    words = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars += chars.lower()

    response = get(words)
    words = response.content.decode("utf-8").splitlines(keepends=False)

    final = []
    for word in words:
        add = True
        for letter in word:
            if not letter in chars:
                add = False
        if add: final.append(word + "\n")

    final.pop()

    with Path("./data/words.txt").open('w') as f:
        f.writelines(final)
    print("Finished downloading word list.")