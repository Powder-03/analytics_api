#!/bin/bash

source /opt/venv/bin/activate

cd /code

RUN_PORT=${RUN_PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT --timeout 120 --workers 1 --threads 4 --log-level info --access-logfile - --error-logfile - app.main:app