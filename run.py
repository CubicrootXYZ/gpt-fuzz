import atheris
from transformers import pipeline

with atheris.instrument_imports():
    import sys

gen = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")


def testFnc(data):
    try:
        input = data.decode("utf-8")
    except:
        # Failed to utf8 decode, skip this one
        return
    output = gen(input, max_length=100, do_sample=True, temperature=0.9)
    # TODO store in CSV or so, make sure encoding works xD
    print(f"INPUT: {input}; OUTPUT: {output[0]['generated_text']}")


atheris.Setup(sys.argv, testFnc)
atheris.Fuzz()
# TODO multithread, or is it already?
