from glob import glob
from transformers import AutoTokenizer

# Load the dialectal and non-dialectal datasets -- see the readme for details.

# Dictionary from dataset names to lists of sentences from that dataset
dataset2text = {}
for file in glob("*/*.txt"):
    dataset = file[:-4]
    print(dataset)
    text = []
    with open("german/de_gsd-ud-dev.txt") as f:
        for line in f:
            text.append(line.strip())
    dataset2text[dataset] = text

# You can inspect some datasets at this point
print("german/de_hdt-ud-dev:",
      len(dataset2text["german/de_hdt-ud-dev"]), "sentences")
print(dataset2text["german/de_hdt-ud-dev"][:3])


# Load a tokenizer, in this case the one for mBERT
# (See readme for some mono- and multilingual tokenizer options)
model_id = 'google-bert/bert-base-multilingual-cased'
tokenizer = AutoTokenizer.from_pretrained(model_id)


# Tokenize the data
text = dataset2text["german/de_hdt-ud-dev"]
token_ids = tokenizer(
    text,
    return_tensors='pt',
    add_special_tokens=False,  # We don't want the [CLS] and [SEP] tokens
    padding=True,  # In order to tokenize multiple sentences at once,
                   # the result needs to have the same number of tokens
                   # -- this is achieved by adding dummy tokens as padding
                   # (token ID: 0, token: [PAD], <pad>, or similar)
).input_ids
# This results in a matrix of token IDs:
# a 2D tensor of size num_sentences x max_tokens_per_sentences.

# In order to also get some information about the tokens themselves
# (like measuring the average length), we can convert the token IDs
# into token forms:
tokens = [[token for token in tokenizer.convert_ids_to_tokens(sent_token_ids)
           if token != tokenizer.pad_token]  # Removing the padding tokens
          for sent_token_ids in token_ids
          ]
print(tokens[:3])

# Now we can compare tokenizers and/or datasets!
# (See instruction PDF.)
