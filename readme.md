### WEBKAOS-Utils

`webkaos-utils` is helpers for working with [webkaos](https://github.com/essentialkaos/webkaos) server.

#### Usage

    Usage: wu command args...
    
    Commands
    
      req-gen host                      Generate RSA key and a certificate signing request
      hpkp-gen csr-file                 Generate HTTP public key pinning (HPKP) header
      ocsp-gen server-cert issuer-cert  Generate OCSP stapling file
      ocsp-check host                   Check OCSP response status for some host
    
    Options
    
      --help, -h                      Show this help message
      --version, -v                   Show information about version

#### License

[EKOL](https://essentialkaos.com/ekol)
