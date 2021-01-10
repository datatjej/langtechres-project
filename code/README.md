# Code

Use this folder for the code related to your project.

MATHiR Threes: https://spraakbanken.gu.se/en/resources/mathir-trad
MATHiR Words: https://spraakbanken.gu.se/en/resources/mathir-ord

## COMMANDS

Normalize:
      
      docker run -v $(pwd):/home mbollmann/norma -s -c example/example.cfg -f example/fnhd_sample.txt
      
Train:

      docker run -v $(pwd):/home mbollmann/norma -c example/example.cfg -f example/fnhd_train.txt -t --saveonexit
      
      
Flags:

`-t` - train only, without generating normalizations <br>
`--saveonexit`- is required (if not given in the config file) to save the trained parametrizations back to the parameter files


## TODO

1. script for extracting all tokens (`form='aff'`) from the MATHir Trees files and saving them in a file, one token per line, called tokens.txt:

\[...\] <br>
aff <br>
iordh <br>
oc <br>
hans <br>
qwinna <br>
\[...\] <br>

2. script for extracting all lemmas (`lemma='af'`) from the MATHiR Tree files:

\[...\] <br>
af <br>
iorþ <br>
ok <br>
han <br>
qvinna <br>
\[...\] <br>

## FINDOUT

1. Is a target lexicon needed for lookuo/mapping normalization? - No!
2. Is a target lexicon needed for weighted Levenshtein distance (WLD) normalization? 
3. Is the parameter file `abc_train.WLD.paramfile` for WLD automatically generated when training on `abc_train.txt`?
4. Is the `abc_train.Mapper.mapfile` automatically generated when training on `abc_train.txt`?
