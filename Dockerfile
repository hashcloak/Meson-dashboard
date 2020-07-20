FROM golang:alpine AS builder
RUN apk update && apk add --no-cache git ca-certificates && \
  update-ca-certificates
WORKDIR /go/mixnet
COPY . .
RUN go build -o /fmixnet /go/mixnet/mixnet.go

FROM python:alpine
RUN apk update && apk add --no-cache g++
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip show dash
COPY --from=builder /fmixnet /bin/fmixnet
COPY ./src/ /app
ENTRYPOINT python /app/app.py
