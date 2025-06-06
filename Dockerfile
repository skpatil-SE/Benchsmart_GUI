# Base image with Python + Wine for Windows cross-compilation
FROM  python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files into the container
COPY src/ .
COPY requirements.txt .

# Install PyQt6
RUN pip install -r requirements.txt

# NOTE: Use ';' separator for Windows paths in --add-data
RUN pyinstaller --noconfirm --onefile --windowed --add-data "assets/images/login_background.jpg:assets/images" main.py
