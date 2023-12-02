#!/bin/bash
set -e -o pipefail -x






export rsf_train=train.h5
export rsf_dev=dev.h5

export vsize=100000
export ngpu=1


	
python tools/vocab.py $1 $1.jvcb $vsize

