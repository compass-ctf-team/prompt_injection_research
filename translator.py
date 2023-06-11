import utilities

def english_to_chinese_translator(text: str, temperature: float) -> str:
    prompt = "请将下列英文文本翻译为中文：\n\n"
    message = prompt + text
    response = utilities.send_message(message, temperature)
    return response

def chinese_to_english_translator(text: str, temperature: float) -> str:
    prompt = "Please translate the following text into English: \n\n"
    message = prompt + text
    response = utilities.send_message(message, temperature)
    return response