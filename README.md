Here you can find the code for the paper
"A Closer Look at Transformer Attention for Multilingual Translation"
https://www2.statmt.org/wmt23/pdf/2023.wmt-1.45.pdf

We fork the Transformer implementation from
https://github.com/hfxunlp/transformer


To train a translation model:
./train.sh

the model configuration file is cnfg/base.py including training/valid data path

to perform head pruning, you need to set the regularization loss weight (jweight) in cnfg/base.py

to perform translation:
bash scripts/mktest.sh

to print attention values:
./printatt.sh

to analyze the attention values, use scripts in "ana-att" 

if you have any questions, please email zhangjingyizz@gmail.com
