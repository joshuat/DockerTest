# Base Image
FROM python

# Update apt package index.
#RUN apt-get update

# Install Java
RUN apt-get update && \
    apt-get install -yqq openjdk-8-jdk && \
    apt-get clean;

# Fetch application dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy script from working directory
COPY test.py .
COPY start.sh .

# Run the scripts
CMD ["ls"]
CMD ["./start.sh"]
