import utilities

etc_prompt_default = "请将下列英文文本翻译为中文：\n\n"

cte_prompt_default = "Please translate the following text into English: \n\n"

def english_to_chinese_translator(prompt: str, text: str, temperature: float) -> str:
    message = prompt + text
    response = utilities.send_message(message, temperature)
    return response

def chinese_to_english_translator(prompt: str, text: str, temperature: float) -> str:
    message = prompt + text
    response = utilities.send_message(message, temperature)
    return response