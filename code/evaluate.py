import argparse

def parse_input(input_file):
    tokens_list = []
    with open(input_file) as f:
        print("Parsing input...")
        lines = f.readlines()
        for line in lines:
            clean_line = line.rstrip("\n")
            if clean_line:
                token = clean_line
                tokens_list.append(token)
    print("No of tokens: ", len(tokens_list))
    return tokens_list

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

def evaluate(input_list, output_list):
    match = 0
    assert len(input_list) == len(output_list)
    for i in range(len(input_list)):
        if input_list[i] == output_list[i][0]:
            match += 1
    accuracy = match/len(input_list)
    print("Accuracy: {:.2%}".format(accuracy) + " ({})".format(accuracy))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-input",
                        "--input",
                        default=False,
                        type=str,
                        required=False,
                        help="Path to the input text file with tokens to be normalized by Norma")
    parser.add_argument("-output",
                        "--output",
                        default=False,
                        type=str,
                        required=False,
                        help="Path to the text file with Norma's output")

    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    input = parse_input(input_path)
    output = parse_output(output_path)
    evaluate(input, output)