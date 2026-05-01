FROM python:3.10-slim

WORKDIR /app

# Copy requirements first
COPY requirements.txt ./

# Install only essential dependencies - no sklearn for faster startup
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY server/ ./server/
COPY students/ ./students/
COPY models.py ./
COPY reward.py ./
COPY openenv.yaml ./

# Expose port
EXPOSE 8000

# Simple startup
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
