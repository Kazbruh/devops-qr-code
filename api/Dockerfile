# Use an official Python 3.13 image as a base
FROM python:3.9

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the requirements.txt file to the working directory
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port 8000 for the FastAPI server
EXPOSE 8000

# Set the default command to run the application
# with uvicorn, using 0.0.0.0 as the host and 80 as the port
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]