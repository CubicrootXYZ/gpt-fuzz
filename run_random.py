# Generates random string inputs of variable length
# and records the outcome.

import csv
import random
import signal
import time
import traceback

import transformers
from transformers import pipeline

transformers.logging.set_verbosity_error()

# Get the base letters, increase likelihood of spaces, etc.
all_letters = [" ", " ", " ", " ", " ", " ", " ", ".", ".", ".", ".", ";", ":"]
for i in range(0, 1100):
    all_letters.append(chr(i))

# Load model
gen = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

# Prepare foo
j = 0
f = open("random.csv", "a")
writer = csv.writer(f, quoting=csv.QUOTE_ALL)


# The function that is fuzzed
def testFnc(data):
    global j
    global f
    j += 1
    output = gen(data, max_length=100, do_sample=True, temperature=0.9)
    writer.writerow([data, output[0]["generated_text"]])

    if j % 100 == 0:
        print(f"{j} inputs tested")


# Random string generator
def get_random_string(length):
    result_str = "".join(random.choice(all_letters) for i in range(length))
    return result_str


def handler(signum, frame):
    f.close()


signal.signal(signal.SIGINT, handler)

# Run forever xD
while True:
    input = get_random_string(random.randint(1, 100))
    try:
        testFnc(input)
    except Exception as e:
        traceback.print_exc()
        print(e)
        print(f"Failed with input: {input}")
        f.close()
        break
