import argparse

def parse_labels(input_file):
    input_tokens = []
    correct_lemmas = []
    with open(input_file) as f:
        print("Parsing input...")
        lines = f.readlines()
        for line in lines:
            clean_line = line.rstrip("\n").split("\t")
            if len(clean_line) > 1:
                token = clean_line[0]
                input_tokens.append(token)
                lemma = clean_line[1]
                correct_lemmas.append(lemma)
    print("No of input tokens: ", len(correct_lemmas))
    return input_tokens, correct_lemmas

def parse_output(output_file):
    output_list = []
    with open(output_file) as f:
        print("Parsing output...")
        lines = f.readlines()
        for line in lines:
            clean_line = line.rstrip("\n").split("\t")
            if len(clean_line) > 1:
                normalized_token = clean_line[0]
                confidence_score = clean_line[1]
                output_list.append((normalized_token, confidence_score))
    print("No of normalized tokens: ", len(output_list))
    return output_list

def evaluate(token_list, label_list, output_list):
    assert len(label_list) == len(output_list)
    match = 0
    failed_match = 0
    with open("../data/matches.txt", "w+") as f1, open("../data/failed_matches.txt", "w+") as f2:
        f1.write("TOKEN\t\t" + "OUTPUT\t\t\t" + "CORRECT\n")
        f2.write("TOKEN\t\t" + "OUTPUT\t\t\t" + "CORRECT\n")
        for i in range(len(label_list)):
            if label_list[i] == output_list[i][0]:
                match += 1
                f1.write(token_list[i] + "\t\t\t" + output_list[i][0] + " ({})".format(output_list[i][1]) + "\t\t\t" + label_list[i] + "\n")
            else:
                f2.write(token_list[i] + "\t\t\t" + output_list[i][0] + " ({})".format(output_list[i][1]) + "\t\t\t" + label_list[i] + "\n")
                failed_match += 1


    accuracy = match/len(token_list)
    print("Matches: {}, Failed matches: {}".format(match, failed_match))
    print("Accuracy: {:.2%}".format(accuracy) + " ({})".format(accuracy))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-input",
                        "--input",
                        default=False,
                        type=str,
                        required=False,
                        help="Path to the text file mathir_train.txt")
    parser.add_argument("-output",
                        "--output",
                        default=False,
                        type=str,
                        required=False,
                        help="Path to the text file with Norma's output")

    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    tokens, labels = parse_labels(input_path)
    output = parse_output(output_path)
    evaluate(tokens, labels, output)