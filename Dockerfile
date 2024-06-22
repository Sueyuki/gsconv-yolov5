# Ultralytics YOLO 🚀, AGPL-3.0 license
# Builds ultralytics/ultralytics:latest image on DockerHub https://hub.docker.com/r/ultralytics/ultralytics
# Image is CUDA-optimized for YOLOv8 single/multi-GPU training and inference

# Start FROM PyTorch image https://hub.docker.com/r/pytorch/pytorch or nvcr.io/nvidia/pytorch:23.03-py3
FROM ultralytics/yolov5
# 设置工作目录
WORKDIR /usr/src/app
COPY . .

# 安装其他必要的依赖
RUN pip install -r requirements.txt
