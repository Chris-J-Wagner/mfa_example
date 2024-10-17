This is a very basic notebook that highlights a simple workflow on how to use the [montreal-forced-aligner](https://montreal-forced-aligner.readthedocs.io/en/latest/), comprising of
- Generating praat {textgrid files, waveform} samples
- Validating the sentence content for out-of-vocabulary (oov) words
- Phonemizing them and adding them to an existing dictionary
- Aligning the waveform with the given transcription

### Installation
run `conda env create -f environment.yaml`
If this fails for some reason, manually create the venv and install the packages via:
```
    conda create -n aligner -c conda-forge montreal-forced-aligner python=3.10
    conda install -c conda-forge montreal-forced-aligner
    pip install speechbrain, num2words, praat-textgrids
```
