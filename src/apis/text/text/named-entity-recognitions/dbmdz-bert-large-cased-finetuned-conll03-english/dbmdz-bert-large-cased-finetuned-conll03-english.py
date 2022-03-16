import torch

from transformers import AutoTokenizer, AutoModelForTokenClassification


def predict(text):
    tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")

    label_list = [
        "O",       # Outside of a named entity
        "B-MISC",  # Beginning of a miscellaneous entity right after another miscellaneous entity
        "I-MISC",  # Miscellaneous entity
        "B-PER",   # Beginning of a person's name right after another person's name
        "I-PER",   # Person's name
        "B-ORG",   # Beginning of an organisation right after another organisation
        "I-ORG",   # Organisation
        "B-LOC",   # Beginning of a location right after another location
        "I-LOC"    # Location
    ]

    # Bit of a hack to get the tokens with the special tokens
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))
    inputs = tokenizer.encode(text, return_tensors="pt")

    outputs = model(inputs)[0]
    predictions = torch.argmax(outputs, dim=2)

    return [(token, label_list[prediction]) for token, prediction in zip(tokens, predictions[0].tolist())]
