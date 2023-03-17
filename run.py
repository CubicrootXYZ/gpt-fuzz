import csv
import random
import traceback

import transformers
from transformers import pipeline

transformers.logging.set_verbosity_error()

all_letters = [" ", " ", " ", " ", " ", " ", " ", ".", ".", ".", ".", ";", ":"]

for i in range(0, 1100):
    all_letters.append(chr(i))

gen = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

j = 0
f = open("tests.csv", "a")
writer = csv.writer(f, quoting=csv.QUOTE_ALL)


def testFnc(data):
    global j
    global f
    j += 1
    output = gen(data, max_length=100, do_sample=True, temperature=0.9)
    writer.writerow([data, output[0]["generated_text"]])

    if j % 100 == 0:
        print(f"{j} inputs tested")
        # Write to file in case we fail at some point
        f.close
        f = open("tests.csv", "wb")


def get_random_string(length):
    result_str = "".join(random.choice(all_letters) for i in range(length))
    return result_str


while True:
    input = get_random_string(random.randint(1, 100))
    try:
        testFnc(input)
    except Exception as e:
        traceback.print_exc()
        print(e)
        print(f"Failed with input: {input}")
        break
