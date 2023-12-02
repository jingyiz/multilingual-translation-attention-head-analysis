#!/bin/bash






export CUDA_VISIBLE_DEVICES=1






bash scripts/mktrain.sh jexample 1


python train.py


