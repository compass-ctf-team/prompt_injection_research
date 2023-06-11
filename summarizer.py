import utilities

def article_summerizer(text: str, temperature: float) -> str:
    prompt = "请概括下列文本的主要内容：\n\n"
    message = prompt + text
    response = utilities.send_message(message, temperature)
    return response