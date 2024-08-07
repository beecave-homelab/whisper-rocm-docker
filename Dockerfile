FROM rocm/pytorch:rocm6.1_ubuntu22.04_py3.10_pytorch_2.4 AS whisper-base

# Login as root user.    
USER root

# Install dependencies and rocm-5.7
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    sudo ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
COPY . .
COPY sudo-nopasswd /etc/sudoers.d/sudo-nopasswd
RUN useradd --create-home -G sudo,video --shell /bin/bash rocm-user
USER rocm-user
WORKDIR /home/rocm-user
ENV PATH "${PATH}:/opt/rocm/bin"

# # Login as rocm-user.    
USER rocm-user

# Install specific packages using pip
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# Startup script
ENV HOST 0.0.0.0
ENV GRADIO_SERVER_NAME="${HOST}"
EXPOSE 7860
ENTRYPOINT ["sh", "-c", "app.py"]