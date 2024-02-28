---
license: other
library_name: peft
tags:
- llama-factory
- lora
- generated_from_trainer
base_model: /data/panfeng/dev/LLM/chatglm3-6b
model-index:
- name: train_2024-02-26-10-48-50
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# train_2024-02-26-10-48-50

This model is a fine-tuned version of [/data/panfeng/dev/LLM/chatglm3-6b](https://huggingface.co//data/panfeng/dev/LLM/chatglm3-6b) on the c2k and the k2c datasets.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- PEFT 0.8.2
- Transformers 4.38.1
- Pytorch 2.0.1
- Datasets 2.17.1
- Tokenizers 0.15.2