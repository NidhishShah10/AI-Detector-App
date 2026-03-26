from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "humarin/chatgpt_paraphraser_on_T5_base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def rewrite_text(text):
    sentences = text.split(". ")
    rewritten_sentences = []

    for sentence in sentences:
        if len(sentence.strip()) < 10:
            continue
        inputs = tokenizer(
            f"paraphrase: {sentence}",
            return_tensors="pt",
            max_length=512,
            truncation=True
        )
        outputs = model.generate(
            **inputs,
            max_length=300,
            num_beams=5,
            num_return_sequences=1
        )
        rewritten = tokenizer.decode(outputs[0], skip_special_tokens=True)
        rewritten_sentences.append(rewritten)

    return ". ".join(rewritten_sentences)

if __name__ == "__main__":
    sample = "Artificial intelligence is transforming education and many industries around the world."
    print("Original:")
    print(sample)
    print("\nRewritten:")
    print(rewrite_text(sample)) ##end