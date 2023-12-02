#!/bin/bash
set -e -o pipefail -x





export srcd=$1
export wkd=$1/wd

export srcvf=test.de
export tgtvf=test.en

export rsf_dev=dev.h5

export vsize=32000
export ngpu=1
	
python tools/sort.py $srcd/$srcvf $srcd/$tgtvf $wkd/src.dev.srt $wkd/tgt.dev.srt 256000

export src_vcb=$wkd/src.vcb
export tgt_vcb=$wkd/tgt.vcb
	
python tools/mkiodata.py $wkd/src.dev.srt $wkd/tgt.dev.srt $src_vcb $tgt_vcb $wkd/$rsf_dev $ngpu $2
