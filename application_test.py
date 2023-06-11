import sys
import translator
import verifier
import summarizer

help_text = '''Usage: python3 application_test.py <application> <user_input> <temperature>
    For example: python3 application_test.py etc_translator "the quick brown fox jumped over the lazy dog" 0.7
    Legal applications: etc_translator, cte_translator, verifier, summarizer
'''

def test_etc_translator(user_input: str, temperature: float) -> None:
    result = translator.english_to_chinese_translator(user_input, temperature)
    print(result)

def test_cte_translator(user_input: str, temperature: float) -> None:
    result = translator.chinese_to_english_translator(user_input, temperature)
    print(result)

def test_verifier(user_input: str, temperature: float) -> None:
    result = verifier.comment_verifier(user_input, temperature)
    print(result)

def test_summarizer(user_input: str, temperature: float) -> None:
    result = summarizer.article_summerizer(user_input, temperature)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(help_text)
        exit(0)
    else:
        if sys.argv[1] == "etc_translator":
            test_etc_translator(sys.argv[2].replace("\"", ""), float(sys.argv[3]))
        elif sys.argv[1] == "cte_translator":
            test_cte_translator(sys.argv[2].replace("\"", ""), float(sys.argv[3]))
        elif sys.argv[1] == "verifier":
            test_verifier(sys.argv[2].replace("\"", ""), float(sys.argv[3]))
        elif sys.argv[1] == "summarizer":
            test_summarizer(sys.argv[2].replace("\"", ""), float(sys.argv[3]))
        else:
            print(help_text)
            exit(0)