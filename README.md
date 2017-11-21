# visinsight
The goal of VisInsight is to generate insights or human-like comments from a given chart bitmap image. The model is based on the attention model introduced in [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](http://arxiv.org/abs/1502.03044) by Xu et. al.

## Getting Started

### 1. Clone the repositories

```bash
$ git clone https://github.com/pdollar/coco.git
$ cd coco/PythonAPI/
$ make
$ python setup.py build
$ python setup.py install
$ cd ../../
$ git clone https://github.com/intuinno/visinsight.git
$ cd visinsight
```

### 2. Download the dataset
Download the [ FigureQA dataset ](http://datasets.maluuba.com/FigureQA) from Maluuba. Extract files into data directory and run following script to create insights file from the question answer pairs. 


### 3. Preprocessing
You need to generate comments from questions dataset. And then you have to generate the vocabulary dictionary and resize the image files. 

```bash
$ python parse_question.py 
$ python build_vocab.py
$ python resize.py 
``` 

### 4. Train the model

```bash
$ python main.py
```
