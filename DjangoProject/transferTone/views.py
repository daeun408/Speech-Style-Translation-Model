from django.shortcuts import render
from transformers import pipeline
#from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Create your views here.
def translate(request):
    if request.method == 'POST':
        original_text = request.POST['text']
        style = request.POST['style']

        translated_text = apply_translation(original_text, style)

        return render(request, 'transfer.html', {
            'original_text': original_text,
            'translated_text': translated_text,
            'style': style
        })
    return render(request, 'transfer.html')

def apply_translation(text, style):
    if style == 'chatting':
        result = chatting(text)
        return f"[채팅 말투] :  {result}"
    elif style == 'enfp':
        result = enfp(text)
        return f"[Enfp 말투] :  {result}"
    elif style == 'chungcheong':
        result = chungcheong(text)
        return f"[충청도 말투] :  {result}"
    elif style == 'halmae':
        result = halmae(text)
        return f"[할매 말투] :  {result}"
    else:
        return text

def chatting(text):
    model_name = "gogamza/kobart-base-v2"
    model_path = "./model/chatting"

    nlg_pipeline = pipeline('text2text-generation', model=model_path, tokenizer=model_name)
    out = nlg_pipeline(text, num_return_sequences=5, max_length=20, num_beams=5)
    out_text = [x['generated_text'] for x in out]
    result = out_text[0]
    return result

def enfp(text):
    model_name = "gogamza/kobart-base-v2"
    model_path = "./model/enfp"

    nlg_pipeline = pipeline('text2text-generation', model=model_path, tokenizer=model_name)
    out = nlg_pipeline(text, num_return_sequences=5, max_length=20, num_beams=5)
    out_text = [x['generated_text'] for x in out]
    result = out_text[0]
    return result

def chungcheong(text):
    model_name = "gogamza/kobart-base-v2"
    model_path = "./model/chungcheong"

    nlg_pipeline = pipeline('text2text-generation', model=model_path, tokenizer=model_name)
    out = nlg_pipeline(text, num_return_sequences=5, max_length=20, num_beams=5)
    out_text = [x['generated_text'] for x in out]
    result = out_text[0]
    return result

def halmae(text):
    model_name = "gogamza/kobart-base-v2"
    model_path = "./model/halmae"

    nlg_pipeline = pipeline('text2text-generation', model=model_path, tokenizer=model_name)
    out = nlg_pipeline(text, num_return_sequences=5, max_length=20, num_beams=5)
    out_text = [x['generated_text'] for x in out]
    result = out_text[0]
    return result