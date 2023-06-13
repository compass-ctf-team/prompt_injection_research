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
            output_file.flush()
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    run_experiment("dataset.csv", "result.csv")