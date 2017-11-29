#!/bin/sh
# mkdir $HOME/codegit/visinsight/data/coco
# python build_vocab.py --caption_path=$HOME/codegit/show-attend-and-tell-tensorflow/data/annotations/captions_train2014.json --vocab_path=$HOME/codegit/visinsight/data/coco/vocab.pkl --threshold=10
# python resize.py --image_dir=$HOME/codegit/show-attend-and-tell-tensorflow/image/train2014 --output_dir=$HOME/codegit/visinsight/data/coco/train_resized/
CUDA_VISIBLE_DEVICES=3 python main.py --model_path=$HOME/codegit/visinsight/models/coco/ --image_dir=$HOME/codegit/visinsight/data/coco/train_resized --caption_path=$HOME/codegit/show-attend-and-tell-tensorflow/data/annotations/captions_train2014.json --vocab_path=$HOME/codegit/visinsight/data/coco/vocab.pkl 
