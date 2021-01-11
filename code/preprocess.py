import os
import argparse
from lxml import etree

def parse_xml(folder_path):

    tokens_list = []
    lemmata_list = []

    for filename in os.listdir(path):
        if not filename.endswith('.xml'): continue
        print("Parsing {}...".format(filename))
        fullname = os.path.join(path, filename)
        tree = etree.parse(fullname)
        root = tree.getroot()

        for elem in root:
            if elem.tag == 'source':
                #print("elem: ", elem)
                for source_elem in elem:
                    if source_elem.tag == 'div':
                        #print("source_elem: ", source_elem)
                        for sent_elem in source_elem:
                            #print("sent_elem: ", sent_elem)
                            if sent_elem.tag == 'sentence':
                                for token_elem in sent_elem:
                                    #print("token_elem: ", token_elem)
                                    if token_elem.tag == 'token':
                                        if 'form' in token_elem.attrib:
                                            token = token_elem.attrib['form']
                                            tokens_list.append(token)
                                        if 'lemma' in token_elem.attrib:
                                            lemma = token_elem.attrib['lemma']
                                            lemmata_list.append(lemma)

    print("Total no of tokens: ", len(tokens_list))

    return tokens_list, lemmata_list

def write_to_textfile(tokens_list, lemmata_list):

    assert len(tokens_list) == len(lemmata_list)
    #f = open("mathir_train.txt", "w+")

    with open("../data/mathir_tokens.txt", "w+") as f1, open("../data/mathir_train.txt", "w+") as f2:
        for i in range(len(tokens_list)):
            f1.write(str(tokens_list[i]) + "\n")
            f2.write(str(tokens_list[i]) + "\t" + str(lemmata_list[i]) + "\n")

    print("Finished writing to {} and {}.".format("mathir_train.txt", "mathir_tokens.txt"))
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

    tokens, lemmata = parse_xml(args.path)
    write_to_textfile(tokens, lemmata)