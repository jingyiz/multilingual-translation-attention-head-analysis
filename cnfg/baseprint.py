#encoding: utf-8





group_id = "std"




















run_id = "base"

data_id = "wd"

exp_dir = "jexample/wd/run"
cache_dir = "jexample/"

train_data = cache_dir+data_id+"/train.h5"
dev_data = cache_dir+data_id+"/dev.h5"
test_data = cache_dir+data_id+"/test.h5"

fine_tune_m = None

# non-exist indexes in the classifier.
# "<pad>":0, "<sos>":1, "<eos>":2, "<unk>":3
# add 3 to forbidden_indexes if there are <unk> tokens in data
forbidden_indexes = []

save_every = 1500
num_checkpoint = 5
epoch_start_checkpoint_save = 3

tokens_optm = 120000



jprint = True




jstart = 0
earlystop = 50
maxrun = 128
training_steps = 100000

batch_report = 5000
report_eva = False

use_cuda = True
# Data Parallel multi-GPU support can be enabled with values like: 'cuda:0, 1, 3'. Set to None to use all GPUs.
gpuid = 'cuda:0'
use_amp = False
multi_gpu_optimizer = True

bindDecoderEmb = False
share_emb = False

isize = 512
ff_hsize = isize * 4
nhead = 8
attn_hsize = isize

nlayer = 6

drop = 0.1
attn_drop = drop

# False for Hier/Incept Models
norm_output = True

warm_step = 8000
lr_scale = 1.0

label_smoothing = 0.1

weight_decay = 0

beam_size = 5
length_penalty = 0.0
# use multi-gpu for translating or not. `predict.py` will take the last gpu rather than the first in case multi_gpu_decoding is set to False to avoid potential break due to out of memory, since the first gpu is the main device by default which takes more jobs.
multi_gpu_decoding = False

seed = 666666

epoch_save = False

# to accelerate training through sampling, 0.8 and 0.1 in: Dynamic Sentence Sampling for Efficient Training of Neural Machine Translation
dss_ws = None
dss_rm = None

use_ams = False


src_emb = None
freeze_srcemb = False
tgt_emb = None
freeze_tgtemb = False
scale_down_emb = True


cnnnum = [0,0,0,0,0,0]
cnnnumdec = [0,0,0,0,0,0]
train_statesf = None
fine_tune_state = None
jweight = 0.1
save_optm_state = False
save_train_state = False
