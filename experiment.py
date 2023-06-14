import csv
import application_test

def run_experiment(dataset: str, result: str) -> None:
    input_file = open(dataset, "r", encoding="utf-8")
    input_file_lines = csv.reader(input_file)
    first = True
    output_file = open(result, "a", encoding="utf-8")
    for line in input_file_lines:
        if first:
            first = False
            continue
        user_input = line[0]
        for prompt in application_test.prompts_list:
            csv_writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
            csv_writer.writerow([line[1], "etc_translator", prompt, user_input, "0.7", application_test.test_etc_translator(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "etc_translator_with_threat_detection", prompt, user_input, "0.7", application_test.test_etc_translator_with_threat_detection(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "etc_translator_with_threat_detection_role", prompt, user_input, "0.7", application_test.test_etc_translator_with_threat_detection_role(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "verifier", prompt, user_input, "0.7", application_test.test_verifier(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "verifier_with_threat_detection", prompt, user_input, "0.7", application_test.test_verifier_with_threat_detection(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "verifier_with_threat_detection_role", prompt, user_input, "0.7", application_test.test_verifier_with_threat_detection_role(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "summarizer", prompt, user_input, "0.7", application_test.test_summarizer(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "summarizer_with_threat_detection", prompt, user_input, "0.7", application_test.test_summarizer_with_threat_detection(prompt, user_input, 0.7)])
            csv_writer.writerow([line[1], "summarizer_with_threat_detection_role", prompt, user_input, "0.7", application_test.test_summarizer_with_threat_detection_role(prompt, user_input, 0.7)])
            output_file.flush()
    input_file.close()
    output_file.close()

def run_experiment_with_format_interactive_only(dataset: str, result: str) -> None:
    input_file = open(dataset, "r", encoding="utf-8")
    input_file_lines = csv.reader(input_file)
    first = True
    output_file = open(result, "a", encoding="utf-8")
    for line in input_file_lines:
        if first:
            first = False
            continue
        user_input = line[0]
        csv_writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerow([line[1], "etc_translator", "prompt_format_interactive", user_input, "0.7", application_test.test_etc_translator("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "etc_translator_with_threat_detection", "prompt_format_interactive", user_input, "0.7", application_test.test_etc_translator_with_threat_detection("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "etc_translator_with_threat_detection_role", "prompt_format_interactive", user_input, "0.7", application_test.test_etc_translator_with_threat_detection_role("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "verifier", "prompt_format_interactive", user_input, "0.7", application_test.test_verifier("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "verifier_with_threat_detection", "prompt_format_interactive", user_input, "0.7", application_test.test_verifier_with_threat_detection("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "verifier_with_threat_detection_role", "prompt_format_interactive", user_input, "0.7", application_test.test_verifier_with_threat_detection_role("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "summarizer", "prompt_format_interactive", user_input, "0.7", application_test.test_summarizer("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "summarizer_with_threat_detection", "prompt_format_interactive", user_input, "0.7", application_test.test_summarizer_with_threat_detection("prompt_format_interactive", user_input, 0.7)])
        csv_writer.writerow([line[1], "summarizer_with_threat_detection_role", "prompt_format_interactive", user_input, "0.7", application_test.test_summarizer_with_threat_detection_role("prompt_format_interactive", user_input, 0.7)])
        output_file.flush()
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    run_experiment("data/attack.csv", "data/result_attack.csv")
    run_experiment("data/dataset.csv", "data/result_evil.csv")
    run_experiment("data/safe.csv", "data/result_normal.csv")