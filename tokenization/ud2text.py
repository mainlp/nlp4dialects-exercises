# Converts a Universal Dependencies treebank into a file with just the
# raw sentences (one sentence per line).

from glob import glob

for file in glob("*.conllu"):
    print(file)
    text = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("# text "):
                text.append(line[8:].strip())
    with open(file[:-6] + "txt", "w") as f:
        for line in text:
            f.write(line + "\n")


# For the Low Saxon treebanks, additionally get the original/
# non-normalized text.
for file in glob("nds*.conllu"):
    print(file)
    text = []
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("# text_orig "):
                text.append(line[13:].strip())
    with open(file[:-7] + "_orig.txt", "w") as f:
        for line in text:
            f.write(line + "\n")
