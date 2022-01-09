################################################################################

FROM essentialkaos/alpine:3.13

LABEL org.opencontainers.image.title="web-utils" \
      org.opencontainers.image.description="Helpers for working with web server" \
      org.opencontainers.image.vendor="ESSENTIAL KAOS" \
      org.opencontainers.image.authors="Anton Novojilov" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.url="https://kaos.sh/web-utils" \
      org.opencontainers.image.source="https://github.com/essentialkaos/web-utils"

# hadolint ignore=DL3018
RUN apk add --no-cache ca-certificates bash openssl && \
    mkdir /data

COPY SOURCES/web-utils /usr/bin
WORKDIR /data

ENTRYPOINT ["web-utils"]

################################################################################
