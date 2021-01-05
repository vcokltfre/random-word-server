from random import sample, choice

from .models import RandomWordData


class WordGenerator:
    def __init__(self):
        with open("./data/words.txt") as f:
            self.words = [word.strip() for word in f.readlines()]

    def generate(self, data: RandomWordData) -> dict:
        num = data.quantity if data.quantity else 1
        num = max(min(1024, num), 1)
        start = data.start_with

        if start:
            valid = [w for w in filter(lambda x: x.startswith(data.start_with), self.words)]
        else:
            valid = self.words

        if len(valid) < num:
            num = len(valid)

        if not num:
            return {"status":"fail", "detail":"Not enough words match the given start_with paramater."}

        if num == 1:
            return {"word":choice(valid)}

        return {"status":"ok", "amount":num, "words":sample(valid, k=num)}