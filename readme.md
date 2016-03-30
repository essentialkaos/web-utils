### WEBKAOS-Utils

`webkaos-utils` is helpers for working with [webkaos](https://github.com/essentialkaos/webkaos) server.

#### Usage

```
Usage: webkaos-utils command args...

Commands

  csr-gen host                         Generate RSA key and a certificate signing request
  hpkp-gen csr|key|crt backup          Generate HTTP public key pinning (HPKP) header
  ocsp-gen server-cert issuer-cert     Generate OCSP stapling file
  ocsp-check host                      Check OCSP response status for some host

Options

  --help, -h                      Show this help message
  --version, -v                   Show information about version

Examples

  webkaos-utils csr-gen domain.com
  Generate RSA key and a certificate signing request for domain.com

  webkaos-utils hpkp-gen domain.com.csr domain.com.backup.key
  Generate HTTP public key pinning (HPKP) header with server and backup pins

  webkaos-utils ocsp-gen sever.crt issuer.crt
  Generate OCSP stapling file using server and issuer certificates

  webkaos-utils ocsp-gen sever-chain.crt
  Generate OCSP stapling file using certificate chain

  webkaos-utils ocsp-check essentialkaos.com
  Check OCSP response status for essentialkaos.com

```

#### License

[EKOL](https://essentialkaos.com/ekol)
