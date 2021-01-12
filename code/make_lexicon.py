import os
import argparse

def extract_lemmas(folder_path):

    lemma_list = []

    for filename in os.listdir(path):
        if not filename.endswith('.tsv'): continue
        print("Parsing {}...".format(filename))
        fullname = os.path.join(path, filename)
        with open(fullname) as f:
            lines = f.readlines()
            for line in lines:
                clean_line = line.rstrip("\n").split("\t")
                if len(clean_line) > 1:
                    lemma = clean_line[0]
                    if lemma not in lemma_list:
                        lemma_list.append(lemma)

    print("Total no of lemmas: ", len(lemma_list))

    return lemma_list

def write_to_textfile(lemma_list):

    with open("../data/sdw_lexicon.txt", "w+") as f:
        for i in range(len(lemma_list)):
            f.write(str(lemma_list[i]) + "\n")

    print("Finished writing to {}.".format("sdw_lexicon.txt"))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-path",
                        "--path",
                        default=False,
                        type=str,
                        required=False,
                        help="Path to the folder with MATHiR Words TSV files")

    args = parser.parse_args()
    path = args.path

    lemmas = extract_lemmas(args.path)
    write_to_textfile(lemmas)