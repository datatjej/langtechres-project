# Code

Use this folder for the code related to your project.

## NORMA COMMANDS

Normalize:

      docker run -v $(pwd):/home mbollmann/norma -s -c example/example.cfg -f example/fnhd_sample.txt

Train:

      docker run -v $(pwd):/home mbollmann/norma -c example/example.cfg -f example/fnhd_train.txt -t --saveonexit
      
Create lexicon files (.fsm and .sym):

      norma_lexicon -w sdw.txt -a sdw.fsm -l sdw.sym -c
      
                                                 norma_lexicon -w de.uniq -a de.fsm -l de.sym -c

Flags:

`-t` - train only, without generating normalizations <br>
`--saveonexit`- is required (if not given in the config file) to save the trained parametrizations back to the parameter files

## PREPROCESS_TREES.PY

This script

For running the code:
1. Download and extract the XML files from MATHiR Threes: https://spraakbanken.gu.se/en/resources/mathir-trad
2. Go to the location where the `preprocess.py` file is located and run: `python3 preprocess.py --path <path_to_mathir_trees_xml_files>`
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

## FINDOUT

1. Is a target lexicon needed for lookup/mapping normalization? - No!
2. Is a target lexicon needed for weighted Levenshtein distance (WLD) normalization? - It runs, but doesn't normalize anything (only returns the unchanged tokens and confidence scores of 0). <br>
3. Is the parameter file `abc_train.WLD.paramfile` for WLD automatically generated when training on `abc_train.txt`? - Yes! (but gives warning)
4. Is the `abc_train.Mapper.mapfile` automatically generated when training on `abc_train.txt`? - Yes, but gives warning: <br>
`*** WARNING: while initializing normalizer Mapper: couldn't open parameter file: /home/example/fnhd_train.Mapper.mapfile`
