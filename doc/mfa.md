# Montreal forced aligner #
### Installation
Run
```
conda env create -f environment.yaml
```
**Fallback** if the above fails:
```
conda create -n mfa python=3.10
conda install -c conda-forge montreal-forced-aligner
conda install pytorch torchvision torchaudio cpuonly -c pytorch
pip install num2words scipy praat-textgrids speechbrain
```

### Components
**Model**:
Installed model via: 
```
mfa model download acoustic german_mfa
```
Installed gp2 model via: 
```
mfa model download g2p german_mfa
```
Installed dictionary via: 
```
mfa model download dictionary german_mfa
```

### Steps for aligning an audio file with a character sequence.
- write the audio files as `.wav` files to a folder
- create a praat-textgrid file for each audio file and store them in the same folder.
See `create_textgrid.ipynb` for an example.
- Validate that each word is in the dictionary. If not, it has to be phonemized using 
the default G2P model and added to the dictionary.