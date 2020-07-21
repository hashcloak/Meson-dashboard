FROM golang:alpine AS builder
RUN apk update && apk add --no-cache \
  git \
  ca-certificates
RUN  update-ca-certificates
WORKDIR /app
COPY go.sum .
COPY go.mod .
RUN go mod download
COPY src/mixnet.go mixnet.go
RUN go build -o fmixnet mixnet.go
