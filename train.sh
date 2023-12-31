#!/bin/bash






export CUDA_VISIBLE_DEVICES=1



mkdir jexample/wd


bash scripts/mktrain.sh jexample 6000


python train.py


