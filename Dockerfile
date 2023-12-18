FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files to the container
COPY fastAPI_model.py .
COPY binary_encoder.joblib .
COPY RFC_model.joblib .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port that FastAPI runs on
EXPOSE 8000

# Command to start the FastAPI server
CMD ["uvicorn", "fastAPI_model:fastAPI_model", "--host", "0.0.0.0", "--port", "8000"]
