from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-large", legacy=False)
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-large")


def generate_ai_description(prompt: str) -> str:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    outputs = model.generate(input_ids, max_new_tokens=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    prompt = input("What you want me to do today?\n")
    print(generate_ai_description(prompt))
