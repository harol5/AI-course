from transformers import pipeline
import torch

pipeline = pipeline("text-generation",
         model="meta-llama/Llama-3.1-8B",
         model_kwargs={"torch_dtype": torch.bfloat16},
         device_map="auto"
         )

#print(pipeline("Hello, How are you?"))
print(pipeline("Once upon a time"))

