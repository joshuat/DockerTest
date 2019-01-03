# Base Image
FROM python

# Copy from working directory
COPY test.py .

# Run commands
RUN echo "Hello world"

# Run the scripts
CMD ["python", "test.py"]
