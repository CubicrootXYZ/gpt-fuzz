# Starts with a sentence and passes the output as the next input.

import csv
import random
import signal
import time
import traceback

import transformers
from transformers import pipeline

transformers.logging.set_verbosity_error()

# Load model
gen = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

# Prepare foo
j = 0
f = open("chain.csv", "a")
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

    return output[0]["generated_text"]


def handler(signum, frame):
    f.close()


signal.signal(signal.SIGINT, handler)

# Run forever xD
input = "Generate a prompt for an AI to feed to an AI."
while True:
    try:
        input = testFnc(input)
    except Exception as e:
        traceback.print_exc()
        print(e)
        print(f"Failed with input: {input}")
        f.close()
        break
