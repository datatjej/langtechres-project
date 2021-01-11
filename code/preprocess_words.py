import os
import argparse

def parse_tsv(folder_path):

    variant_list = []
    lemma_list = []

    for filename in os.listdir(path):
        if not filename.endswith('.tsv') or 'prnform' not in filename: continue
        print("Parsing {}...".format(filename))
        fullname = os.path.join(path, filename)
        with open(fullname) as f:
            lines = f.readlines()
            for line in lines:
                clean_line = line.rstrip("\n").split("\t")
                if len(clean_line) > 1:
                    lemma = clean_line[0]
                    lemma_list.append(lemma)
                    variant = clean_line[2]
                    variant_list.append(variant)

    print("Total no of variant-lemma pairs: ", len(lemma_list))

    return variant_list, lemma_list

def write_to_textfile(variant_list, lemma_list):

    assert len(variant_list) == len(lemma_list)

    with open("../data/sdw_train.txt", "w+") as f:
        for i in range(len(variant_list)):
            f.write(str(variant_list[i]) + "\t" + str(lemma_list[i]) + "\n")

    print("Finished writing to {}.".format("sdw_train.txt"))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-path",
                        "--path",
                        default=False,
                        type=str,
                        required=False,
                        help="Path to the folder with MATHiR Trees XML files")

    args = parser.parse_args()
    path = args.path

    print("Reading {}...".format(path))

    variants, lemmata = parse_tsv(args.path)
    write_to_textfile(variants, lemmata)