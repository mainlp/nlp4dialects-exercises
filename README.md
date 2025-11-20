# Spelling variation & tokenization

First, please **read the PDF with the instructions**. 

This repo contains data and code to get you started. The files in the `arabic`, `german`, `greek`, and `italian` are sourced from Universal Dependencies datasets that are described below.
For working with the CODET data, see `demo_code_paralleldata.ipynb`.

The tokenizers listed here are by no means a comprehensive list, and you're welcome to also try out others.

## (Some) multilingual tokenizers

- https://huggingface.co/google-bert/bert-base-multilingual-cased (languages: https://github.com/google-research/bert/blob/master/multilingual.md#list-of-languages -- includes some non-standard varieties)
- https://huggingface.co/FacebookAI/xlm-roberta-base (languages: https://github.com/facebookresearch/fairseq/tree/main/examples/xlmr#introduction)

## Arabic

Standard
- ar_pud-ud-test: Modern Standard Arabic, CC BY-SA 3.0, https://github.com/UniversalDependencies/UD_Arabic-PUD

Non-standard
- ajp_madar-ud-test: South Levantine Arabic, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_South_Levantine_Arabic-MADAR
- If you would like to use additional Arabic data, you can download the [AraBench](https://alt.qcri.org/resources1/mt/arabench/) dataset.

Tokenizers
- https://huggingface.co/aubmindlab/bert-base-arabertv2

## German

Standard
- de_gsd-ud-...: German, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_German-GSD/
- de_hdt-ud-...: German, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_German-HDT/
- de_pud-ud-test: German, CC BY-SA 3.0, https://github.com/UniversalDependencies/UD_German-PUD/

Non-standard
- bar_maibaam-ud-test: Bavarian (multiple Bavarian dialects), CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Bavarian-MaiBaam
- gsw_divital-ud-test: Alemannic (Alsatian), CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Alemannic-DIVITAL/
- gsw_uzh-ud-test: Alemannic (Swiss German), CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Alemannic-UZH/
- nds_lsdc-ud-orig-...: Low Saxon (ad-hoc spelling), CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Low_Saxon-LSDC
- nds_lsdc-ud-norm-...: Low Saxon (the same dataset, but normalized using the Nysassiske Skryvwyse), CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Low_Saxon-LSDC

Other standardized languages -- for comparison to see how the German tokenization compares to dialectal vs. non-dialectal tokenization for related varieties, and as a potential other standard language for Low Saxon
- nl_alpino-ud-train: Dutch, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Dutch-Alpino/
- nl_lassysmall-ud-train: Dutch, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Dutch-LassySmall

Tokenizers
- https://huggingface.co/deepset/gbert-base (German)
- https://huggingface.co/dbmdz/bert-base-german-cased (German)
- https://huggingface.co/google-bert/bert-base-german-cased (German)
- https://huggingface.co/GroNLP/bert-base-dutch-cased (Dutch)

## Greek

Standard
- el_gdt-ud-...: Modern Greek, CC BY-NC-SA 3.0, https://github.com/UniversalDependencies/UD_Greek-GDT
- el_gud-ud-...: Modern Greek, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Greek-GUD/

Non-standard
- cpg_amgic-ud-test: Cappadocian, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Cappadocian-AMGiC
- cpg_tuecl-ud-test: Pharasiot, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Cappadocian-TueCL/
- el_cretan-ud-...: Cretan Greek, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Greek-Cretan/
- el_lesbian-ud-test: Lesbian Greek, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Greek-Lesbian/
- el_messinian-ud-...: Messinian Greek, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Greek-Messinian/

Tokenizer
- https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1

## Italian

Standard
- it_isdt-ud-...: Italian, CC BY-NC-SA 3.0, https://github.com/UniversalDependencies/UD_Italian-ISDT/
- it_vit-ud-train: Italian (the dataset refers to Venice, but doesn't seem to contain Venetian data), CC BY-NC-SA 3.0, https://github.com/UniversalDependencies/UD_Italian-VIT

Non-standard
- lij_glt-ud-...: Ligurian (Genoese), C-UDA 1.0, https://github.com/UniversalDependencies/UD_Ligurian-GLT/
- nap_rb-ud-test: Neapolitan, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Neapolitan-RB/
- scn_stb-ud-test: Sicilian, CC BY-SA 4.0, https://github.com/UniversalDependencies/UD_Sicilian-STB/

Tokenizer
- https://huggingface.co/dbmdz/bert-base-italian-cased
- https://huggingface.co/dlicari/Italian-Legal-BERT

## General note

The text data mentioned in this readme is from the Universal Dependencies project (https://universaldependencies.org/), release 2.17.
To get more information about the individual datasets (data source, genre, preprocessing decisions, links to publications), go to the GitHub repositories linked above.

Links to the licenses:
- CC BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0/deed.en
- CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/deed.en
- CC BY-NC-SA 3.0: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
- C-UDA 1.0: https://github.com/UniversalDependencies/UD_Ligurian-GLT/blob/master/LICENSE.txt

