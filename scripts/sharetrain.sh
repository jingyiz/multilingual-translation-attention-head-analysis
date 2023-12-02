#!/bin/bash
set -e -o pipefail -x


export srcd=$1
export wkd=$2
export srctf=$3
export tgttf=$4
export srcvf=$5
export tgtvf=$6

export rsf_train=train.h5
export rsf_dev=dev.h5

export vsize=100000
export ngpu=1
python tools/sort.py $srcd/$srctf $srcd/$tgttf $wkd/src.train.srt $wkd/tgt.train.srt 500
	
python tools/sort.py $srcd/$srcvf $srcd/$tgtvf $wkd/src.dev.srt $wkd/tgt.dev.srt 256000

export src_vcb=$wkd/tgt.vcb
export tgt_vcb=$wkd/tgt.vcb
	
cat $wkd/src.train.srt $wkd/tgt.train.srt > $wkd/srctgt.train.srt
python tools/vocab.py $wkd/srctgt.train.srt $tgt_vcb $vsize
	
python tools/mkiodata.py $wkd/src.train.srt $wkd/tgt.train.srt $src_vcb $tgt_vcb $wkd/$rsf_train $ngpu
python tools/mkiodata.py $wkd/src.dev.srt $wkd/tgt.dev.srt $src_vcb $tgt_vcb $wkd/$rsf_dev $ngpu
