from transformers import AutoTokenizer
from transformers import pipeline
from dataclasses import dataclass
import os
from src.logger import logging
from transformers import pipeline

@dataclass
class PredictionConfig:
    model_path:str = os.path.join('data\pegasus-samsum-model') 
    tokenizer_path:str = os.path.join('data\tokenizer')

class Prediction:
    def __init__(self, config: PredictionConfig):
        self.config = config

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        model = pipeline('summarization', model=self.config.model_path, tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = model(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:") 
        print(output)

        return output
    
