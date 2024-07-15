# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the project
COPY . .

# Run the tests
CMD ["pytest"]
