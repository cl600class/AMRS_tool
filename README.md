# DSP_Final
A simple automatic meeting record & summarization tool. (3 participants)
## Requirements
- Python >= 3.7.4
  - PyAudio
  - SpeechRecognition
  - TextRank4ZH   (reference: https://www.letiantian.me/2014-12-01-text-rank/)
    - jieba >= 0.35
    - numpy >= 1.7.1
    - networkx >= 1.9.1
- Microphone
- Internet Connection
- (Optional) Replace the original ```stopwords.txt``` in ```.../site-packages/textrank4zh/``` for traditional Chinese support.
## Files
- record.py: record the voice of the participants & process by Google Speech Recognition
- convert.py: transform the meeting transcript into individual transcripts
- summarize.py: for all the individual transcripts, perform TextRank respectively
## Run
- Run the main program
```console
  $ bash main.sh
```
- Sample

  <img src="https://i.imgur.com/iAuW5JK.gif" width="300" height="495">
## Output
- The meeting transcript will be named ```f.txt```
- The transcripts corresponding to the 3 participants will be stored in ```output/```
- The summarized text file will be stored in ```summary/```
## Tested Environment
- MacOS 10.14.6
- zsh
- Blue Yeti Microphone
