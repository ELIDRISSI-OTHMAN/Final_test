FROM continuumio/miniconda3:latest

WORKDIR /app

# Copy environment file and create conda environment
COPY environment.yml .
RUN conda env create -f environment.yml

# Upgrade libstdc++ and install other dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libstdc++6 \
        build-essential \
        libgl1 \
        libegl1 \
        libglib2.0-0 \
        libxkbcommon0 \
        libxrender1 \
        libxext6 \
        libxcb1 \
        libxi6 \
        libfontconfig1 \
        libdbus-1-3 && \
    rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . .

# Expose port
EXPOSE 8000

# Activate conda environment and run app
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate stitcher && python main.py"]

