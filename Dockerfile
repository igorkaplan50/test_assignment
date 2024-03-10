FROM python:slim

EXPOSE 8081

# Install dependencies
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean

# Install requirements
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Run as non-root
RUN groupadd -r lendbuzz && useradd --no-log-init -r -g lendbuzz lendbuzz
RUN  mkdir -p /app && chown -R lendbuzz /app

USER lendbuzz
ENV PYTHONPATH=/app
# Add app
COPY central_service.py /app/
COPY common.py /app
COPY services.json /app

WORKDIR /app
CMD ["gunicorn", "-b", "0.0.0.0:8081", "central_service:app"]
