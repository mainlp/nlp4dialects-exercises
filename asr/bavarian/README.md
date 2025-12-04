# Dialect ASR: German and Bavarian audios

## Usage note & references
The audio files we share with you (see next section) aren't officially released yet. *Don't* share them with others or upload them where others can access them. *Don't* use them for any purposes other than this seminar exercise.

For more information on the files, see
> Standard-to-Dialect Transfer Trends Differ across Text and Speech: A Case Study on Intent and Topic Classification in German Dialects. Blaschke, Winkler & Plank. Unpublished preprint, 2025. https://arxiv.org/abs/2510.07890

The gold-standard written versions are from the already existing dataset xSID (https://github.com/mainlp/xsid, CC BY-SA 4.0). The CC BY-SA 4.0 license also applies to the text files we share here.

The German (and English) text files are from:

> From Masked Language Modeling to Translation: Non-English Auxiliary Tasks Improve Zero-shot Spoken Language Understanding (van der Goot et al., NAACL 2021) https://aclanthology.org/2021.naacl-main.197/

The Bavarian text file is from:

> Slot and Intent Detection Resources for Bavarian and Lithuanian: Assessing Translations vs Natural Queries to Digital Assistants (Winkler et al., LREC-COLING 2024) https://aclanthology.org/2024.lrec-main.1297/

## Audio and text files

This folder contains a subset of xSID's test set. Each instance corresponds to one sentence directed to a virtual assistant (typically a question or command). The sentences were independently translated from English to German and Bavarian, which is why the syntax and word choice may differ between the translations (even beyond dialect-related syntactic/lexical differences). A few of the original English sentences contain language errors, which may be reflected in the translations.

We will share the audio files with you via the Slack channel for today's exercise.
The audio files were recorded by the same speaker for German and Bavarian. They demonstrate a "best-case" scenario for ASR: the audios are scripted text that is read out loud (instead of representing spontaneous utterances), recorded with a good microphone and without background noise.

Audio files for trying your hand at (manual) speech-to-text transcription -- transcribe them in German and/or Bavarian before listening to the German versions or reading the text files:
- xsid_audio_bar_test_003.wav
- xsid_audio_bar_test_107.wav
- xsid_audio_bar_test_158.wav
- xsid_audio_bar_test_171.wav
- xsid_audio_bar_test_336.wav

## ASR outputs

The `asr_outputs` folder contains transcriptions by several different ASR models in case you would like to compare outputs across models.

The following two models use connectionist temporal classification (CTC) for decoding their hidden representations into text. For today's session, you only need to know that this results in outputs that are relatively close to the spoken input on a sound/character level. (If you'd like to read up on this after class, you can do so here: https://distill.pub/2017/ctc/.)

- AndrewMcDowell-wav2vec2-xls-r-300m-german-de: https://huggingface.co/AndrewMcDowell/wav2vec2-xls-r-300m-german-de, a version of [XSL-R 300M](https://huggingface.co/facebook/wav2vec2-xls-r-300m) fine-tuned on German ASR data
- facebook-mms-1b-all: https://huggingface.co/facebook/mms-1b-all,  amodel fine-tuned on (some) ASR data in >1k languages

The Whisper models use language modelling for decoding instead. Here, they are sorted from the smallest to the largest model in the series:
- openai-whisper-tiny: https://huggingface.co/openai/whisper-tiny
- openai-whisper-base: https://huggingface.co/openai/whisper-base
- openai-whisper-small: https://huggingface.co/openai/whisper-small
- openai-whisper-medium: https://huggingface.co/openai/whisper-medium
- openai-whisper-large-v3: https://huggingface.co/openai/whisper-large-v3
