# Code

Use this folder for the code related to your project.

## NORMA COMMANDS

Normalize:

      docker run -v $(pwd):/home mbollmann/norma -s -c example/example.cfg -f example/fnhd_sample.txt

Train:

      docker run -v $(pwd):/home mbollmann/norma -c example/example.cfg -f example/fnhd_train.txt -t --saveonexit
      
Create lexicon files (.fsm and .sym)

      docker run -v $(pwd):/home --entrypoint norma_lexicon mbollmann/norma -w sdw_lexicon.txt -a sdw_lexicon.fsm -l sdw_lexicon.sym -c
      
Flags:

`-t` - train only, without generating normalizations <br>
`--saveonexit`- is required (if not given in the config file) to save the trained parametrizations back to the parameter files

## PREPROCESS_TREES.PY

This script parses the MATHiR Trees  text into two files, one with tokens and one with tokens + lemmas.

For running the code:
1. Download and extract the XML files from MATHiR Threes: https://spraakbanken.gu.se/en/resources/mathir-trad
2. Go to the location where the `preprocess_trees.py` file is located and run: `python3 preprocess_trees.py --path <path_to_mathir_trees_xml_files>`
3. This will create two text files in the `data` folder:<br>
* `mathir_tokens.txt`, which contains all tokens from all five files (including duplicates): <br>
*hær* <br>
*sigx* <br>
*aff* <br>
*abotum* <br>
*allum* <br>
\[...\] <br>

* `mathir_train.txt`, which contains all tokens and their corresponding lemma from all five files: <br>
*hær	här* <br>
*sigx	sighia* <br>
*aff	af* <br>
*abotum     abbote* <br>
*allum	alder* <br>
\[...\] <br>

## PREPROCESS_WORDS.PY

This script parses the MATHiR Words files and creates a file with variant-lemma pairs.

For running the code:
1. Download and extract the text files from MATHiR Words: https://spraakbanken.gu.se/en/resources/mathir-ord
2. Go to the location where the `preprocess_words.py` file is located and run: `python3 preprocess_words.py --path <path_to_mathir_words_text_files>`
3. This will create a text file called `sdw_train.txt` in the `data` folder.<br>

## MAKE_LEXICON.PY

This script parses the MATHiR Words files and creates a file with only the lemmas. To be used for creating target lexicons.

For running the code:
1. Download and extract the text files from MATHiR Words: https://spraakbanken.gu.se/en/resources/mathir-ord
2. Go to the location where the `make_lexicon.py` file is located and run: `python3 make_lexicon.py --path <path_to_mathir_words_text_files>`
3. This will create a text file called `sdw_lexicon.txt` in the `data` folder.<br>

## BASELINE.PY

This script takes the `mathir_train.txt` file produced by `preprocess_trees.py` as input (currently using my path, go in and change that if you want to use it yourself) to control how many of the tokens are already the same as the lemma. An accuracy score is printed out to the terminal.

## EVALUATE.PY

This script takes the output text file by Norma and the `mathir_train.txt` file as input and compares what Norma outputted to the correct labels. An accuracy score is printed in the terminal. Go to the directory where `evaluate.py`is located and run: 

      python3 evaluate.py --input <path_to_mathir_train.txt> --output <path_to_normas_output_file>

## FINDOUT

1. Is a target lexicon needed for lookup/mapping normalization? - No!
2. Is a target lexicon needed for weighted Levenshtein distance (WLD) normalization? - It runs, but doesn't normalize anything (only returns the unchanged tokens and confidence scores of 0). <br>
3. Is the parameter file `abc_train.WLD.paramfile` for WLD automatically generated when training on `abc_train.txt`? - Yes! (but gives warning)
4. Is the `abc_train.Mapper.mapfile` automatically generated when training on `abc_train.txt`? - Yes, but gives warning: <br>
`*** WARNING: while initializing normalizer Mapper: couldn't open parameter file: /home/example/fnhd_train.Mapper.mapfile`
