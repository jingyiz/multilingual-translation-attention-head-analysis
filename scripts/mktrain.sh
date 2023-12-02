#!/bin/bash
set -e -o pipefail -x










export srcd=$1
export wkd=$1/wd
export srctf=train.de
export tgttf=train.en
export srcvf=valid.de
export tgtvf=valid.en

export rsf_train=train.h5
export rsf_dev=dev.h5

export vsize=32000
export ngpu=1
python tools/sort.py $srcd/$srctf $srcd/$tgttf $wkd/src.train.srt $wkd/tgt.train.srt 500
	
python tools/sort.py $srcd/$srcvf $srcd/$tgtvf $wkd/src.dev.srt $wkd/tgt.dev.srt 256000

export src_vcb=$wkd/src.vcb
export tgt_vcb=$wkd/tgt.vcb
	
python tools/vocab.py $wkd/src.train.srt $src_vcb $vsize
python tools/vocab.py $wkd/tgt.train.srt $tgt_vcb $vsize
	
python tools/mkiodata.py $wkd/src.train.srt $wkd/tgt.train.srt $src_vcb $tgt_vcb $wkd/$rsf_train $ngpu $2
python tools/mkiodata.py $wkd/src.dev.srt $wkd/tgt.dev.srt $src_vcb $tgt_vcb $wkd/$rsf_dev $ngpu $2
