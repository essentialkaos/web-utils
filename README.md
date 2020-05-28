<p align="center"><a href="#readme"><img src="https://gh.kaos.st/webkaos-utils.svg"/></a></p>

<p align="center">
  <a href="https://travis-ci.com/essentialkaos/webkaos-utils"><img src="https://travis-ci.com/essentialkaos/webkaos-utils.svg"></a>
  <a href="https://essentialkaos.com/ekol"><img src="https://gh.kaos.st/ekol.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`webkaos-utils` is helpers for working with [webkaos](https://github.com/essentialkaos/webkaos) server.

### Installation

#### From ESSENTIAL KAOS Public repo for RHEL7/CentOS7

```
[sudo] yum install -y yum install -y https://yum.kaos.st/kaos-repo-latest.el7.noarch.rpm
[sudo] yum install webkaos-utils
```

#### From GitHub repository

```bash
wget https://kaos.sh/webkaos-utils/SOURCES/webkaos-utils
chmod +x webkaos-utils
[sudo] mv webkaos-utils /usr/bin/
```

Also, you can use the latest version of utility without installation:

```bash
bash <(curl -fsSL https://kaos.sh/webkaos-utils/SOURCES/webkaos-utils) # pass options here
```

### Usage

```
Usage: webkaos-utils command args…

Commands

  csr-gen host                        Generate RSA key and a certificate signing request
  csr-info csr                        Print info from certificate signing request
┌ hpkp-gen csr backup                 Generate HTTP public key pinning (HPKP) header from CSR file
│ hpkp-gen key backup                 Generate HTTP public key pinning (HPKP) header from KEY file
└ hpkp-gen crt backup                 Generate HTTP public key pinning (HPKP) header from CRT file
┌ ocsp-gen server-cert issuer-cert    Generate OCSP stapling file from server certificate
└ ocsp-gen cert-chain                 Generate OCSP stapling file from server certificate chain
  ocsp-check host server-name         Check OCSP response status for some host
  0rtt-check host server-name         Check 0-RTT support

Options

  --ecc, -E        Generate ECC certificate signing request
  --help, -h       Show this help message
  --version, -v    Show information about version

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

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![Build Status](https://travis-ci.org/essentialkaos/webkaos-utils.svg?branch=master)](https://travis-ci.org/essentialkaos/webkaos-utils) |
| `develop` | [![Build Status](https://travis-ci.org/essentialkaos/webkaos-utils.svg?branch=develop)](https://travis-ci.org/essentialkaos/webkaos-utils) |

### License

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
