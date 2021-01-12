match = 0
no_tokens = 0
with open("/mnt/c/Users/tovae/Desktop/git_projects/norma/doc/example/mathir_test/mathir_train.txt") as f:
    lines = f.readlines()
    for line in lines:
        clean_line = line.rstrip("\n").split("\t")
        if len(clean_line) > 1:
            no_tokens += 1
            token = clean_line[0]
            lemma = clean_line[1]
            if token == lemma:
                match += 1


accuracy = match/no_tokens
print("Basline Accuracy: ", accuracy)