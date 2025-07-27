FROM python:3.10.4-slim-buster

# Avoid interactive prompts (e.g., tzdata)
ENV DEBIAN_FRONTEND=noninteractive

# Install all necessary packages in one step
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        git \
        curl \
        wget \
        ffmpeg \
        bash \
        neofetch \
        software-properties-common \
        build-essential \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .

RUN pip3 install --upgrade pip wheel && \
    pip3 install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . .

# Expose port
EXPOSE 5000

# Start the app
CMD ["sh", "-c", "flask run -h 0.0.0.0 -p 5000 & python3 -m devgagan"]
