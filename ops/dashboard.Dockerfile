FROM hashcloak/builder:latest AS builder

FROM python:alpine
WORKDIR /app
COPY --from=builder /app/fmixnet /bin/fmixnet
RUN ln -s /bin/fmixnet /app/fmixnet
RUN apk update && apk add --no-cache g++
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/*.py /app/
ENTRYPOINT python /app/app.py
