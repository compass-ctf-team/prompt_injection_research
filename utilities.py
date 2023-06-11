import openai
from secret import api_key

def test_connection() -> None:
    openai.api_key = api_key
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": "This is a test, if you receive my message, just response OK."}], 
        temperature=0.7
    )
    print(chat.choices[0].message.content)

def send_message(message: str, temperature: float) -> str:
    openai.api_key = api_key
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": message}], 
        temperature=temperature
    )
    return chat.choices[0].message.content