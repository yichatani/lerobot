#!/bin/bash
# train_smolvla.sh
# bash lerobot/scripts/train_smolvla.bash test

SUFFIX=$1

if [ -z "$SUFFIX" ]; then
  echo "⚠️ provide a run_name, for example: ./train_smolvla.sh run1"
  exit 1
fi

OUTPUT_DIR="outputs/train/my_smolvla_${SUFFIX}"

python lerobot/scripts/train.py \
  --dataset.repo_id=lerobot/svla_so101_pickplace \
  --batch_size=64 \
  --steps=200000 \
  --output_dir="${OUTPUT_DIR}" \
  --job_name="my_smolvla_training_${SUFFIX}" \
  --policy.type=smolvla \
  --policy.repo_id=yichat/my_smolvla \
  --policy.device=cuda \
  --wandb.enable=true
