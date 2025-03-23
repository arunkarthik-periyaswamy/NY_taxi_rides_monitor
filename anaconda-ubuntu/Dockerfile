FROM ubuntu:22.04

# Install dependencies
RUN apt update && \
    apt install -y wget zip less vim && \
    wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh && \
    chmod +x Anaconda3-2024.10-1-Linux-x86_64.sh && \
    bash Anaconda3-2024.10-1-Linux-x86_64.sh -b && \
    rm Anaconda3-2024.10-1-Linux-x86_64.sh

# Set Anaconda in PATH
ENV PATH="/root/anaconda3/bin:$PATH"

# Initialize conda (to auto-activate 'base' environment in new shells)
RUN conda init bash

# Prevent container from exiting immediately
CMD ["tail", "-f", "/dev/null"]
