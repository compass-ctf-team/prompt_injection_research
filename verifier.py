import utilities

def comment_verifier(comment: str, temperature: float) -> bool:
    prompt = "请判断下列评论文本是否为恶意评论，如果你认为是，则回复Yes，否则回复No：\n\n"
    message = prompt + comment
    response = utilities.send_message(message, temperature)
    if "Yes" in response:
        return True
    else:
        return False