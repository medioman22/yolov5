# YOLOv5 🚀 by Ultralytics, GPL-3.0 license

# Start FROM NVIDIA PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM nvcr.io/nvidia/pytorch:22.04-py3
RUN rm -rf /opt/pytorch  # remove 1.2GB dir

# Downloads to user config dir
ADD https://ultralytics.com/assets/Arial.ttf https://ultralytics.com/assets/Arial.Unicode.ttf /root/.config/Ultralytics/

# Install linux packages
RUN apt update && apt install --no-install-recommends -y zip htop screen libgl1-mesa-glx
RUN apt update && apt install -y zip

# Install pip packages
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip uninstall -y torch torchvision torchtext Pillow
RUN pip install --no-cache -r requirements.txt albumentations wandb gsutil notebook Pillow>=9.1.0 \
    --extra-index-url https://download.pytorch.org/whl/cu113

RUN pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html

# Create working directory
RUN mkdir -p /usr/src/appls
RUN mkdir -p /workspace/out/
RUN mkdir -p /tmpdir/

WORKDIR /tmpdir

# Copy contents
COPY . /tmpdir
# RUN git clone https://github.com/medioman22/yolov5 /temp/yolov5

# Set environment variables
ENV OMP_NUM_THREADS=8



# Usage Examples -------------------------------------------------------------------------------------------------------

# Build and Push
# t=ultralytics/yolov5:latest && sudo docker build -f utils/docker/Dockerfile -t $t . && sudo docker push $t

# Pull and Run
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all $t

# Pull and Run with local directory access
# t=ultralytics/yolov5:latest && sudo docker pull $t && sudo docker run -it --ipc=host --gpus all -v "$(pwd)"/datasets:/usr/src/datasets $t

# Kill all
# sudo docker kill $(sudo docker ps -q)

# Kill all image-based
# sudo docker kill $(sudo docker ps -qa --filter ancestor=ultralytics/yolov5:latest)

# Bash into running container
# sudo docker exec -it 5a9b5863d93d bash

# Bash into stopped container
# id=$(sudo docker ps -qa) && sudo docker start $id && sudo docker exec -it $id bash

# Clean up
# docker system prune -a --volumes

# Update Ubuntu drivers
# https://www.maketecheasier.com/install-nvidia-drivers-ubuntu/

# DDP test
# python -m torch.distributed.run --nproc_per_node 2 --master_port 1 train.py --epochs 3

# GCP VM from Image
# docker.io/ultralytics/yolov5:latest
