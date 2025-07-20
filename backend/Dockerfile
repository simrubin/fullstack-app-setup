FROM python:3.9

# Set working directory
WORKDIR /app

# Create virtual environment in a standard location
RUN python -m venv /opt/venv

# Ensure virtualenv binaries are used by default
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies using virtualenv pip
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Expose Flask default port
EXPOSE 5000

# Default command
CMD ["python", "app.py"]