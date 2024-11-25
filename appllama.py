# GEMMA_GGUF_PATH = r'C:\Users\Dante\.cache\huggingface\hub\models--google--gemma-2b-it\snapshots\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\gemma-2b-it.gguf'
# GEMMA_GGUF_PATH = 'C:\\Users\\Dante\\.cache\\huggingface\\hub\\models--google--gemma-2b-it\\snapshots\\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\\gemma-2b-it.gguf'
# $env:LIBROT_GUFF_PATH  = 'C:\\Users\\Dante\\.cache\\huggingface\\hub\\models--google--gemma-2b-it\\snapshots\\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\\gemma-2b-it.gguf'


### Starting librot
# A lots of guff for sentence similarity https://huggingface.co/leliuga/all-MiniLM-L12-v2-GGUF/tree/main
# $env:LIBROT_GPT_GUFF_PATH = 'C:\\Users\\Dante\\.cache\\huggingface\\hub\\models--google--gemma-2b-it\\snapshots\\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\\gemma-2b-it.gguf'
# $env:LIBROT_GPT_GUFF_PATH  = 'C:\\Users\\Dante\\Documents\\Personal Files\\guff_files\\mistral-7b-openorca.Q2_K.gguf'
# $env:LIBROT_SENT_TRANS_GUFF_PATH  = 'C:\\Users\\Dante\\Documents\\Personal Files\\guff_files\\all-MiniLM-L12-v2.F32.gguf'
# $env:LIBROT_SECRET_KEY  = 'librot-django-insecure-key'

# from huggingface_hub import hf_hub_download
# from llama_cpp import Llama

# ## Define model name and file name
# model_name = "google/gemma-2b-it"
# model_file = "gemma-2b-it.gguf"


# ## Download the model
# # model_path = hf_hub_download(model_name, filename=model_file)


# model_kwargs = {
#   "n_ctx":4096,    # Context length to use
#   "n_threads":4,   # Number of CPU threads to use
#   "n_gpu_layers":0,# Number of model layers to offload to GPU. Set to 0 if only using CPU
# }

# ## Instantiate model from downloaded file
# llm = Llama(model_path=GEMMA_GGUF_PATH, **model_kwargs)

# ## Generation kwargs
# generation_kwargs = {
#     "max_tokens":500, # Max number of new tokens to generate
#     "stop":["<|endoftext|>", "</s>"], # Text sequences to stop generation on
#     "echo":False, # Echo the prompt in the output
#     "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
# }

# ## Run inference
# import datetime
# print(f'LLAMA START: {datetime.datetime.now()}')
# prompt = "The meaning of life is "
# res = llm(prompt, **generation_kwargs) # Res is a dictionary

# ## Unpack and the generated text from the LLM response dictionary and print it
# # print(res["choices"][0]["text"])
# print('res: ', res)
# print(f'LLAMA END: {datetime.datetime.now()}')



# LLAMA START: 2024-03-02 10:27:54.112553
# LLAMA END: 2024-03-02 10:29:10.652100
# {
#    "id":"cmpl-9b5669c1-7ae5-4c97-b8e3-02f4862916a0",
#    "object":"text_completion",
#    "created":1709356812,
#    "model":"C:\\Users\\Dante\\.cache\\huggingface\\hub\\models--google--gemma-2b-it\\snapshots\\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\\gemma-2b-it.gguf",
#    "choices":[
#       {
#          "text":"\n\n**Philosophical:**\n\n* **Existentialism:** Life is inherently meaningless and that we are ultimately alone in the universe.\n* **Nihilism:** Life is devoid of purpose or meaning.\n* **Stoicism:** Life is not something to be controlled or possessed, and that acceptance of fate is the only meaningful thing.\n* **Humanism:** Life is a precious gift that should be lived to its fullest potential.\n\n**Religious:**\n\n* **Christianity:** Jesus died on the cross to atone for human sin, offering salvation and meaning to those who believe in him.\n* **Islam:** Life is a sacred gift from God, and those who lose their lives in the name of God will be rewarded with eternal bliss.\n* **Hinduism:** Life is a cycle of reincarnation, with each life offering an opportunity for spiritual growth and liberation.\n\n**Personal:**\n\n* **Self-discovery:** Life is a journey of self-discovery and exploration.\n* **Relationships:** Love and connection with others can provide meaning and purpose.\n* **Meaningful work:** Contributing to something larger than oneself can give life a sense of purpose.\n* **Personal growth:** Striving for personal growth and self-improvement can lead to a sense of fulfillment.\n\nUltimately, the meaning of life is a matter of individual belief and perspective. It can be found through philosophical contemplation, religious faith, personal reflection, or a combination of these approaches.",
#          "index":0,
#          "logprobs":"None",
#          "finish_reason":"stop"
#       }
#    ],
#    "usage":{
#       "prompt_tokens":7,
#       "completion_tokens":295,
#       "total_tokens":302
#    }
# }



##### ------------------------------ CHAT COMPLETION ------------------------------
LIBROT_GPT_GUFF_PATH  = 'C:\\Users\\Dante\\Documents\\Personal Files\\guff_files\\mistral-7b-openorca.Q2_K.gguf'
# GEMMA_GGUF_PATH = r'C:\Users\Dante\.cache\huggingface\hub\models--google--gemma-2b-it\snapshots\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\gemma-2b-it.gguf'
from llama_cpp import Llama
import datetime
import json


llm = Llama(
      model_path=LIBROT_GPT_GUFF_PATH, #GEMMA_GGUF_PATH
      chat_format="llama-2",
      verbose=False,
      )
print(f'LLAMA START: {datetime.datetime.now()}')
res = llm.create_chat_completion(
        messages = [
            {
                "role": "system", 
                "content": "You are an intelligence analyst who is well verse with  Intelligence Community Directive 203."
            },
            # {
            #     "role": "user",
            #     "content": "Describe what is life."
            # },
            # {
            #     "role":"assistant",
            #     "content":"\n\nLife, in its essence, is a complex tapestry woven from innumerable threads of biological processes, cognitive experiences, and existential questions. It is a journey through time marked by both fleeting moments of joy and profound moments of sorrow, laughter, and introspection. It is a constant dance between the physical and the mental, the tangible and the intangible, the finite and the infinite.\n\nLife is not merely the sum of our experiences or the product of our genes. It is a vibrant and dynamic force that compels us to question our existence, explore the world around us, and discover the meaning of our lives. It is a continuous exploration of the boundaries between self and other, between the individual and the collective, between the finite and the infinite.\n\nLife is a precious gift, a treasure to be cherished and protected. It is a reminder that we are all interconnected beings, part of something larger than ourselves. Through life's ups and downs, we learn to appreciate the beauty of the present moment, to find solace in the simple pleasures, and to cultivate compassion for those around us.\n\nUltimately, life is about living fully, embracing the present moment, and leaving a positive impact on the world. It is about contributing to something greater than ourselves, leaving behind a legacy that will inspire future generations."
            # },
            {
                "role": "user",
                "content": """
                    I will give you an article, get all the person entity names and repond in the following json format below. Respond only by the format asked. Make data as empty list [] if none is found.
                    
                    FORMAT:
                    {
                        "data": [
                            {"firstName": "some name", "lastName": "some lastname"}
                        ]
                    }

                    ARTICLE:
                    Sam and Dean Winchester are brothers and the main protagonists of Supernatural. They are dedicated to one another, though there are many instances of strain throughout the series. Their relationship developed as one of the show's main plot lines.
                    Dante is a fan of them.
                    
                    """
            },
        ],
        # stream = True
        # functions= [
        #     {
        #       "name": "get_name",
        #       "description": "Get the name",
        #       "parameters": {
        #         "type": "object",
        #         "properties": {
        #           "firstName": {
        #             "type": "string",
        #             "description": "First name"
        #           },
        #           "lastName": {
        #             "type": "string",
        #             "description": "last name"
        #           },
        #           "fullName": {
        #             "type": "string",
        #             "description": "Full name"
        #           }
        #         },
        #         "required": ["fullName"]
        #       }
        #     }
        #   ],
        # function_call= "auto",
        response_format={ "type": "json_object" },
    )
print('res:', res)
content_response = res['choices'][0]['message']['content']
print('content_response:', content_response)
json_content_response=json.loads(content_response)
print('json_content_response:', json_content_response)
# listed_content_response = list(content_response)
# print('LLL:', l)
# for l in listed_content_response:
#     print('LLL:', l)

# for r in res:
#     print('RRR:', r)
print(f'LLAMA END: {datetime.datetime.now()}')


### --- Sample response ---
# {
#    "id":"chatcmpl-eb05f3c5-7941-48d6-be0e-1af12516ad70",
#    "object":"chat.completion",
#    "created":1709356168, # unix time stamp time.time()
#    "model":"C:\\Users\\Dante\\.cache\\huggingface\\hub\\models--google--gemma-2b-it\\snapshots\\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\\gemma-2b-it.gguf",
#    "choices":[
#       {
#          "index":0,
#          "message":{
#             "role":"assistant",
#             "content":"\n\nLife, in its essence, is a complex tapestry woven from innumerable threads of biological processes, cognitive experiences, and existential questions. It is a journey through time marked by both fleeting moments of joy and profound moments of sorrow, laughter, and introspection. It is a constant dance between the physical and the mental, the tangible and the intangible, the finite and the infinite.\n\nLife is not merely the sum of our experiences or the product of our genes. It is a vibrant and dynamic force that compels us to question our existence, explore the world around us, and discover the meaning of our lives. It is a continuous exploration of the boundaries between self and other, between the individual and the collective, between the finite and the infinite.\n\nLife is a precious gift, a treasure to be cherished and protected. It is a reminder that we are all interconnected beings, part of something larger than ourselves. Through life's ups and downs, we learn to appreciate the beauty of the present moment, to find solace in the simple pleasures, and to cultivate compassion for those around us.\n\nUltimately, life is about living fully, embracing the present moment, and leaving a positive impact on the world. It is about contributing to something greater than ourselves, leaving behind a legacy that will inspire future generations."
#          },
#          "finish_reason":"stop"
#       }
#    ],
#    "usage":{
#       "prompt_tokens":31,
#       "completion_tokens":259,
#       "total_tokens":290
#    }
# }



# from huggingface_hub import hf_hub_download
# repo_id="google/gemma-2b-it"
# guff_filename="gemma-2b-it.gguf"
# model_path = hf_hub_download(repo_id, filename=guff_filename)
# print('model_path: ', model_path)
# import os
# os.environ['LIBROT_GUFF_PATH'] = model_path


# curl -X POST http://localhost:8000/generate-response/ \     -H "Content-Type: application/json" \     -d '{"user_prompt": "What is a model"}'



# message_thread
# - name 

# messages
# - role (user/bot) 
# - created datetime
# - message
# - prompt_tokens int
# - completion_tokens
# - total_tokens
# - message_thread_id


# {
#    "id":"chatcmpl-eb05f3c5-7941-48d6-be0e-1af12516ad70",
#    "object":"chat.completion",
#    "created":1709356168, # unix time stamp time.time()
#    "model":"C:\\Users\\Dante\\.cache\\huggingface\\hub\\models--google--gemma-2b-it\\snapshots\\718cb189da9c5b2e55abe86f2eeffee9b4ae0dad\\gemma-2b-it.gguf",
#    "choices":[
#       {
#          "index":0,
#          "message":{
#             "role":"assistant",
#             "content":"\n\nLife, in its essence, is a complex tapestry woven from innumerable threads of biological processes, cognitive experiences, and existential questions. It is a journey through time marked by both fleeting moments of joy and profound moments of sorrow, laughter, and introspection. It is a constant dance between the physical and the mental, the tangible and the intangible, the finite and the infinite.\n\nLife is not merely the sum of our experiences or the product of our genes. It is a vibrant and dynamic force that compels us to question our existence, explore the world around us, and discover the meaning of our lives. It is a continuous exploration of the boundaries between self and other, between the individual and the collective, between the finite and the infinite.\n\nLife is a precious gift, a treasure to be cherished and protected. It is a reminder that we are all interconnected beings, part of something larger than ourselves. Through life's ups and downs, we learn to appreciate the beauty of the present moment, to find solace in the simple pleasures, and to cultivate compassion for those around us.\n\nUltimately, life is about living fully, embracing the present moment, and leaving a positive impact on the world. It is about contributing to something greater than ourselves, leaving behind a legacy that will inspire future generations."
#          },
#          "finish_reason":"stop"
#       }
#    ],
#    "usage":{
#       "prompt_tokens":31,
#       "completion_tokens":259,
#       "total_tokens":290
#    }
# }


#---------------- TODO ----------------
# 1. add threadpoolexecutor on chunk searching


# RESPONSE FORMAT:
#                     {
#                         "data": [
#                             {"firstName": "some name", "lastName": "some lastname"}
#                         ]
#                     }

#                     EXAMPLE RESPONSE:
#                     {
#                         "data": [
#                             {"firstName": "Jane", "lastName": "Doe"},
#                             {"firstName": "John", "lastName": "Doe"},
#                         ]
#                     }

