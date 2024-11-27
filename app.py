#####--------------------------- START DOCU -------------------------
Using huggingface transformer library

### Huggingface welcome
#$ pip install huggingface_hub				
# You already have it if you installed transformers or datasets
#$ huggingface-cli login
# Log in using a token from huggingface.co/settings/tokens
#$ Create a model or dataset repo from the CLI if needed
						

### huggingface-cli repo create repo_name --type {model, dataset, space}
### May need to login
# from huggingface_hub import login
# login()
# hf_GNXqNye_SOME_TOKEN_BVsdj #readonly and already deleted on HF


# pip install --upgrade pip
# pip install -U transformers
# pip install tensorflow # please use torch for gemma
# pip install torch
# pip install accelerate #

#####--------------------------- END DOCU -------------------------

# from transformers import AutoTokenizer, AutoModelForCausalLM
# import datetime

# print(f'START: {datetime.datetime.now()}')

# GEMMA_7B = "google/gemma-7b"
# GEMMA_2B = "google/gemma-2b-it" #"google/gemma-2b"

# # print(f'loading model start: {datetime.datetime.now()}')
# tokenizer = AutoTokenizer.from_pretrained(GEMMA_2B)
# model = AutoModelForCausalLM.from_pretrained(GEMMA_2B) #device_map="auto"
# # print(f'loading model end: {datetime.datetime.now()}')

# # print(f'loading tokenizer start: {datetime.datetime.now()}')
# input_text = "Can you write me a pyton method that add two integer, but return a string oops if the result is odd number. Reply only with the answern and don't include my original question. Also, can you tell me the difference between class ng module?"
# input_ids = tokenizer(input_text, return_tensors="pt")
# # print(f'loading tokenizer end: {datetime.datetime.now()}')

# print(f'generate start: {datetime.datetime.now()}')
# outputs = model.generate(**input_ids, max_length=200)
# print('outputs: ', tokenizer.decode(outputs[0]))

# print(f'END: {datetime.datetime.now()}')




###############################################
### JUST A SAMPLE BASIC USING DEFAULT MODEL
###############################################
# from transformers import pipeline
# classifier = pipeline('sentiment-analysis')
# res = classifier('I am sad')
# print(res)


###############################################
### USING GPT-2 - just a text generation to continue the initial text
###############################################

# from transformers import pipeline, set_seed
# import datetime
# print(f'GPT-2 START: {datetime.datetime.now()}')
# generator = pipeline('text-generation', model='gpt2')
# set_seed(42)
# result = generator("Write me something about Machine Learning article", max_length=10, num_return_sequences=5, truncation=True)
# print(f'GPT-2 result: {result}')
# print(f'GPT-2 END: {datetime.datetime.now()}')



###################G2#####################################
# "Can you write me a pyton method that add two integer, but return a string oops if the result is odd number."
# START: 2024-02-24 16:42:49.832954
# END: 2024-02-24 16:45:18.843192
# outputs:  <bos>Can you write me a pyton method that add two integer, but return a string oops if the result is odd number.

# Answer:

# def add_two_integers(a, b): if a % 2 == 0: return a + b else: return a + b + 1
# def add_two_integers(a, b): if a % 2 == 0: return a + b else: return a + b + 1<eos>

###################G7#####################################
# "Can you write me a pyton method that add two integer, but return a string oops if the result is odd number."
# START: 2024-02-24 16:46:55.102058
# END: 2024-02-24 17:20:02.249812
# outputs:  <bos>Can you write me a pyton method that add two integer, but return a string oops if the result is odd number.

# Answer:

# def add_two_integers(a, b): if a == b: return "oops"
# else: return str(a + b)<eos>



LIBROT_GPT_GUFF_PATH  = 'C:\\Users\\Dante\\Documents\\Personal Files\\guff_files\\mistral-7b-openorca.Q2_K.gguf'

from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
import datetime

tokenizer = AutoTokenizer.from_pretrained(LIBROT_GPT_GUFF_PATH)
# model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it", device_map="auto")
model = AutoModelForCausalLM.from_pretrained(LIBROT_GPT_GUFF_PATH)
streamer = TextStreamer(tokenizer)

input_text = "Write me a poem about Machine Learning."
input_text = "The meaning of life is"

input_ids = tokenizer(input_text, return_tensors="pt")
print(f'generate start: {datetime.datetime.now()}')
outputs = model.generate(**input_ids,  max_length=200, streamer=streamer)
print(tokenizer.decode(outputs[0]))
print(f'END: {datetime.datetime.now()}')
