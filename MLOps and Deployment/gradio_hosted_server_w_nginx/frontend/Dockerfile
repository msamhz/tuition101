# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
# Copy only the requirements.txt initially to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the current directory contents into the container at /usr/src/app
COPY . .

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "gradio_interface.py"]
