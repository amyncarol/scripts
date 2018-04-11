#!/bin/bash
#SBATCH --job-name=gpu_test
#SBATCH --account=fc_mdasta
#SBATCH --partition=savio2_gpu
#SBATCH --qos=savio_debug
#SBATCH --time=00:30:00

#SBATCH --nodes=1

#Number of GPUs, this can be in the format of "gpu:[1-4]", or "gpu:K80:[1-4] with the type included
#SBATCH --gres=gpu:1

# Number of tasks (one for each GPU desired for use case) (example):
#SBATCH --ntasks=1

# Processors per task (please always specify the total number of processors twice the number of GPUs):
#SBATCH --cpus-per-task=2

module load ml/tensorflow/1.0.0-py36
python cifar10_multi_gpu_train.py --num_gpus=1
