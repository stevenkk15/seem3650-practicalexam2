"""
Configuration for training on Python code dataset.
"""

# data
dataset = 'code_generation'
out_dir = 'out-code-generation'

# model
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

# training
batch_size = 64
block_size = 256
gradient_accumulation_steps = 1
max_iters = 5000
eval_interval = 500
eval_iters = 200
log_interval = 10

# optimizer
learning_rate = 1e-3
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
warmup_iters = 100
lr_decay_iters = 5000
min_lr = 1e-4

# system
device = 'cuda'   # 'cuda' or 'cpu'
compile = True    # use torch.compile if available
