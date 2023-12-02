#!/bin/bash

    
export CUDA_VISIBLE_DEVICES=0,1
    
cd $2

    
python ppnotab $1
   
