#encoding: utf-8



import sys

import numpy
import h5py





from utils.fmt.base import ldvocab
from utils.fmt.dual import batch_padder

from cnfg.ihyp import *


















def handle(finput, ftarget, fvocab_i, fvocab_t, frs, minbsize=1,bsize=1, expand_for_mulgpu=True,  maxpad=max_pad_tokens_sentence, maxpart=normal_tokens_vs_pad_tokens, maxtoken=3*max_tokens_gpu, minfreq=False, vsize=False):
	vcbi, nwordi = ldvocab(fvocab_i, minf=minfreq, omit_vsize=vsize, vanilla=False)
	vcbt, nwordt = ldvocab(fvocab_t, minf=minfreq, omit_vsize=vsize, vanilla=False)
	if expand_for_mulgpu:
		_bsize = bsize * minbsize
		_maxtoken = maxtoken * minbsize
	else:
		_bsize = bsize
		_maxtoken = maxtoken
	rsf = h5py.File(frs, 'w')
	src_grp = rsf.create_group("src")
	tgt_grp = rsf.create_group("tgt")
	curd = 0
	for i_d, td in batch_padder(finput, ftarget, vcbi, vcbt, _bsize, maxpad, maxpart, _maxtoken, minbsize):
		rid = numpy.array(i_d, dtype=numpy.int32)
		rtd = numpy.array(td, dtype=numpy.int32)
		#rld = numpy.array(ld, dtype=numpy.int32)
		wid = str(curd)
		src_grp.create_dataset(wid, data=rid, **h5datawargs)
		tgt_grp.create_dataset(wid, data=rtd, **h5datawargs)
		#rsf["l" + wid] = rld
		curd += 1
	rsf["ndata"] = numpy.array([curd], dtype=numpy.int32)
	rsf["nword"] = numpy.array([nwordi, nwordt], dtype=numpy.int32)
	rsf.close()
	print("Number of batches: %d\nSource Vocabulary Size: %d\nTarget Vocabulary Size: %d" % (curd, nwordi, nwordt,))

if __name__ == "__main__":
	handle(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]),int(sys.argv[7]))
