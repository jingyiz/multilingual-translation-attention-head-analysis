#!/bin/bash

























set -e -o pipefail -x
export srcd=jexample
export srctf=test.de
export modelf=jexample/wd/runwd/std/base/last.h5

export ngpu=1
export tgtd=jexample/wd

export bpef=out.bpe
export src_vcb=$tgtd/src.vcb
export tgt_vcb=$tgtd/tgt.vcb

python tools/sorti.py $srcd/$srctf $tgtd/$srctf.srt
python tools/mktest.py $tgtd/$srctf.srt $src_vcb $tgtd/test.h5 $ngpu
python predict.py $tgtd/$bpef.srt $tgt_vcb $modelf
python tools/restore.py $srcd/$srctf $tgtd/$srctf.srt $tgtd/$bpef.srt $tgtd/$bpef
	
