# visinsight
The goal of VisInsight is to generate insights or human-like comments from a given chart bitmap image. The model is based on the attention model introduced in [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](http://arxiv.org/abs/1502.03044) by Xu et. al.

## Getting Started

### Prerequisites
Download the [ FigureQA dataset ](http://datasets.maluuba.com/FigureQA) from Maluuba. Extract files into data directory and run following script to create insights file from the question answer pairs. 

```bash
$ cd visinght
$ pip install -r requirements.txt
$ python parse_question.py --insight_path='insight file path' --question_path='qa_pairs.json file path'
``` 


