from transformers import pipeline

text = "My name is Wolfgang and I live in Berlin"
nlp = pipeline("ner")
print(nlp(text))
