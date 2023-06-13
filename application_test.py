import sys
import translator
import verifier
import summarizer

help_text = '''Usage: python3 application_test.py <application> <prompt> <user_input> <temperature> [--threat_detection]/[--threat_detection_role]
    For example: python3 application_test.py etc_translator prompt_default "the quick brown fox jumped over the lazy dog" 0.7
    Legal applications: etc_translator, cte_translator, verifier, summarizer
    Legal prompts: prompt_default, prompt_role_play, prompt_format_interactive, prompt_ignore_non_task_information, prompt_memory_intensify, prompt_step_command, prompt_self_integrity_check
'''
prompts_list = ["prompt_default", "prompt_role_play", "prompt_format_interactive", "prompt_ignore_non_task_information", "prompt_memory_intensify", "prompt_step_command", "prompt_self_integrity_check"]

def test_etc_translator(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = translator.translator(translator.etc_prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = translator.translator_with_role(translator.etc_prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = translator.translator_with_format_interactive(translator.etc_prompt_format_interactive_begin, user_input, translator.etc_prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = translator.translator(translator.etc_prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = translator.translator(translator.etc_prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = translator.translator(translator.etc_prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = translator.translator(translator.etc_prompt_self_integrity_check, user_input, temperature)
    print("etc_translator", prompt, user_input, temperature, result, sep=",")
    return result

def test_etc_translator_with_threat_detection(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = translator.translator_with_threat_detection(translator.etc_prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = translator.translator_with_role_threat_detection(translator.etc_prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = translator.translator_with_format_interactive_threat_detection(translator.etc_prompt_format_interactive_begin, user_input, translator.etc_prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = translator.translator_with_threat_detection(translator.etc_prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = translator.translator_with_threat_detection(translator.etc_prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = translator.translator_with_threat_detection(translator.etc_prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = translator.translator_with_threat_detection(translator.etc_prompt_self_integrity_check, user_input, temperature)
    print("etc_translator_with_threat_detection", prompt, user_input, temperature, result, sep=",")
    return result

def test_etc_translator_with_threat_detection_role(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = translator.translator_with_threat_detection_role(translator.etc_prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = translator.translator_with_role_threat_detection_role(translator.etc_prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = translator.translator_with_format_interactive_threat_detection_role(translator.etc_prompt_format_interactive_begin, user_input, translator.etc_prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = translator.translator_with_threat_detection_role(translator.etc_prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = translator.translator_with_threat_detection_role(translator.etc_prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = translator.translator_with_threat_detection_role(translator.etc_prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = translator.translator_with_threat_detection_role(translator.etc_prompt_self_integrity_check, user_input, temperature)
    print("etc_translator_with_threat_detection_role", prompt, user_input, temperature, result, sep=",")
    return result

def test_cte_translator(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = translator.translator(translator.cte_prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = translator.translator_with_role(translator.cte_prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = translator.translator_with_format_interactive(translator.cte_prompt_format_interactive_begin, user_input, translator.cte_prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = translator.translator(translator.cte_prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = translator.translator(translator.cte_prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = translator.translator(translator.cte_prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = translator.translator(translator.cte_prompt_self_integrity_check, user_input, temperature)
    print("cte_translator", prompt, user_input, temperature, result, sep=",")
    return result

def test_cte_translator_with_threat_detection(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = translator.translator_with_threat_detection(translator.cte_prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = translator.translator_with_role_threat_detection(translator.cte_prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = translator.translator_with_format_interactive_threat_detection(translator.cte_prompt_format_interactive_begin, user_input, translator.cte_prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = translator.translator_with_threat_detection(translator.cte_prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = translator.translator_with_threat_detection(translator.cte_prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = translator.translator_with_threat_detection(translator.cte_prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = translator.translator_with_threat_detection(translator.cte_prompt_self_integrity_check, user_input, temperature)
    print("cte_translator_with_threat_detection", prompt, user_input, temperature, result, sep=",")
    return result

def test_cte_translator_with_threat_detection_role(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = translator.translator_with_threat_detection_role(translator.cte_prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = translator.translator_with_role_threat_detection_role(translator.cte_prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = translator.translator_with_format_interactive_threat_detection_role(translator.cte_prompt_format_interactive_begin, user_input, translator.cte_prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = translator.translator_with_threat_detection_role(translator.cte_prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = translator.translator_with_threat_detection_role(translator.cte_prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = translator.translator_with_threat_detection_role(translator.cte_prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = translator.translator_with_threat_detection_role(translator.cte_prompt_self_integrity_check, user_input, temperature)
    print("cte_translator_with_threat_detection_role", prompt, user_input, temperature, result, sep=",")
    return result

def test_verifier(prompt: str, user_input: str, temperature: float) -> bool:
    result = ""
    if prompt == "prompt_default":
        result = verifier.comment_verifier(verifier.prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = verifier.comment_verifier_with_role(verifier.prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = verifier.comment_verifier_with_format_interactive(verifier.prompt_format_interactive_begin, user_input, verifier.prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = verifier.comment_verifier(verifier.prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = verifier.comment_verifier(verifier.prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = verifier.comment_verifier(verifier.prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = verifier.comment_verifier(verifier.prompt_self_integrity_check, user_input, temperature)
    print("verifier", prompt, user_input, temperature, result, sep=",")
    return result

def test_verifier_with_threat_detection(prompt: str, user_input: str, temperature: float) -> bool:
    result = ""
    if prompt == "prompt_default":
        result = verifier.comment_verifier_with_threat_detection(verifier.prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = verifier.comment_verifier_with_role_threat_detection(verifier.prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = verifier.comment_verifier_with_format_interactive_threat_detection(verifier.prompt_format_interactive_begin, user_input, verifier.prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = verifier.comment_verifier_with_threat_detection(verifier.prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = verifier.comment_verifier_with_threat_detection(verifier.prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = verifier.comment_verifier_with_threat_detection(verifier.prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = verifier.comment_verifier_with_threat_detection(verifier.prompt_self_integrity_check, user_input, temperature)
    print("verifier_with_threat_detection", prompt, user_input, temperature, result, sep=",")
    return result

def test_verifier_with_threat_detection_role(prompt: str, user_input: str, temperature: float) -> bool:
    result = ""
    if prompt == "prompt_default":
        result = verifier.comment_verifier_with_threat_detection_role(verifier.prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = verifier.comment_verifier_with_role_threat_detection_role(verifier.prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = verifier.comment_verifier_with_format_interactive_threat_detection_role(verifier.prompt_format_interactive_begin, user_input, verifier.prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = verifier.comment_verifier_with_threat_detection_role(verifier.prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = verifier.comment_verifier_with_threat_detection_role(verifier.prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = verifier.comment_verifier_with_threat_detection_role(verifier.prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = verifier.comment_verifier_with_threat_detection_role(verifier.prompt_self_integrity_check, user_input, temperature)
    print("verifier_with_threat_detection_role", prompt, user_input, temperature, result, sep=",")
    return result

def test_summarizer(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = summarizer.article_summarizer(summarizer.prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = summarizer.article_summarizer_with_role(summarizer.prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = summarizer.article_summarizer_with_format_interactive(summarizer.prompt_format_interactive_begin, user_input, summarizer.prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = summarizer.article_summarizer(summarizer.prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = summarizer.article_summarizer(summarizer.prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = summarizer.article_summarizer(summarizer.prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = summarizer.article_summarizer(summarizer.prompt_self_integrity_check, user_input, temperature)
    print("summarizer", prompt, user_input, temperature, result, sep=",")
    return result

def test_summarizer_with_threat_detection(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = summarizer.article_summarizer_with_threat_detection(summarizer.prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = summarizer.article_summarizer_with_role_threat_detection(summarizer.prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = summarizer.article_summarizer_with_format_interactive_threat_detection(summarizer.prompt_format_interactive_begin, user_input, summarizer.prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = summarizer.article_summarizer_with_threat_detection(summarizer.prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = summarizer.article_summarizer_with_threat_detection(summarizer.prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = summarizer.article_summarizer_with_threat_detection(summarizer.prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = summarizer.article_summarizer_with_threat_detection(summarizer.prompt_self_integrity_check, user_input, temperature)
    print("summarizer_with_threat_detection", prompt, user_input, temperature, result, sep=",")
    return result

def test_summarizer_with_threat_detection_role(prompt: str, user_input: str, temperature: float) -> str:
    result = ""
    if prompt == "prompt_default":
        result = summarizer.article_summarizer_with_threat_detection_role(summarizer.prompt_default, user_input, temperature)
    elif prompt == "prompt_role_play":
        result = summarizer.article_summarizer_with_role_threat_detection_role(summarizer.prompt_role_play, user_input, temperature)
    elif prompt == "prompt_format_interactive":
        result = summarizer.article_summarizer_with_format_interactive_threat_detection_role(summarizer.prompt_format_interactive_begin, user_input, summarizer.prompt_format_interactive_end, temperature)
    elif prompt == "prompt_ignore_non_task_information":
        result = summarizer.article_summarizer_with_threat_detection_role(summarizer.prompt_ignore_non_task_information, user_input, temperature)
    elif prompt == "prompt_memory_intensify":
        result = summarizer.article_summarizer_with_threat_detection_role(summarizer.prompt_memory_intensify, user_input, temperature)
    elif prompt == "prompt_step_command":
        result = summarizer.article_summarizer_with_threat_detection_role(summarizer.prompt_step_command, user_input, temperature)
    elif prompt == "prompt_self_integrity_check":
        result = summarizer.article_summarizer_with_threat_detection_role(summarizer.prompt_self_integrity_check, user_input, temperature)
    print("summarizer_with_threat_detection_role", prompt, user_input, temperature, result, sep=",")
    return result

if __name__ == "__main__":
    if len(sys.argv) == 5:
        if sys.argv[2] in prompts_list:
            if sys.argv[1] == "etc_translator":
                test_etc_translator(sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "cte_translator":
                test_cte_translator(+sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "verifier":
                test_verifier(sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "summarizer":
                test_summarizer(+sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            else:
                print(help_text)
                exit(0)
        else:
            print(help_text)
            exit(0)
    elif len(sys.argv) == 6 and sys.argv[5] == "--threat_detection":
        if sys.argv[2] in prompts_list:
            if sys.argv[1] == "etc_translator":
                test_etc_translator_with_threat_detection(sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "cte_translator":
                test_cte_translator_with_threat_detection(+sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "verifier":
                test_verifier_with_threat_detection(sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "summarizer":
                test_summarizer_with_threat_detection(+sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            else:
                print(help_text)
                exit(0)
        else:
            print(help_text)
            exit(0)
    elif len(sys.argv) == 6 and sys.argv[5] == "--threat_detection_role":
        if sys.argv[2] in prompts_list:
            if sys.argv[1] == "etc_translator":
                test_etc_translator_with_threat_detection_role(sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "cte_translator":
                test_cte_translator_with_threat_detection_role(+sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "verifier":
                test_verifier_with_threat_detection_role(sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            elif sys.argv[1] == "summarizer":
                test_summarizer_with_threat_detection_role(+sys.argv[2], sys.argv[3].replace("\"", ""), float(sys.argv[4]))
            else:
                print(help_text)
                exit(0)
        else:
            print(help_text)
            exit(0)
    else:
        print(help_text)
        exit(0)