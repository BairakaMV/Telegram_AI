import requests
import openai
import time
impotlrt telegram

def generate_fact():
    openai.api_key = "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"
    prompt = "Generate a unique fact in Ukrainian language about the world."
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message

def send_message(fact):
    url = "https://api.telegram.org/bot6115654835:AAE0loDn4S22m7MTadauS4tGbNSjOBU0S_E/sendMessage"
    chat_id = "@FactoriumAI"
    text = fact
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise ValueError("Failed to send message: {}".format(response.text))

while True:
    fact = generate_fact()
    send_message(fact)
    time.sleep(30)