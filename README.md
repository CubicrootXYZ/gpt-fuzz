# GPT-Fuzz

This repo contains files to fuzz a GPT neo model from [Hugging Face](https://huggingface.co/EleutherAI/gpt-neo-125M). 

The fuzzing is very primitive and just generates random string inputs for the model. This is no serious approach in "cracking" the model or finding bugs in the stack. I was only curious what such a model would do with some random input. 

## Running it

Install python 3 and pip. Run `install.sh`.

Run one of the `run_xxx.py` files. They will generate a CSV file with the in- and outputs.