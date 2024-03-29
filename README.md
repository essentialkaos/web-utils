<p align="center"><a href="#readme"><img src="https://gh.kaos.st/web-utils.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/web-utils/ci"><img src="https://kaos.sh/w/web-utils/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#license">License</a></p>

<br/>

`web-utils` is helpers for working with web server.

### Installation

#### From ESSENTIAL KAOS Public repository

```
sudo yum install -y https://yum.kaos.st/get/$(uname -r).rpm
sudo yum install web-utils
```

#### From GitHub repository

```bash
curl https://kaos.sh/web-utils/SOURCES/web-utils -o web-utils
chmod +x web-utils
sudo mv web-utils /usr/bin/
```

Also, you can use the latest version of utility without installation:

```bash
bash <(curl -fsSL https://kaos.sh/web-utils/SOURCES/web-utils) # pass your options here
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/web-utils.git
cd web-utils
sudo make install
```

#### Using Docker

The latest version of `web-utils` also available as Docker image on [DockerHub](https://kaos.sh/d/web-utils) and [GitHub Container Registry](https://kaos.sh/p/web-utils).

```bash
docker run --rm -it -v "$(pwd):/data" essentialkaos/web-utils:latest # pass your options here
```

or

```bash
docker run --rm -it -v "$(pwd):/data" ghcr.io/essentialkaos/web-utils:latest # pass your options here
```

### Usage

```
Usage: web-utils command args…

Commands

┌ csr-gen host                        Generate key and a certificate signing request
└ csr-gen config                      Generate key and a certificate signing request from OpenSSL configuration file
  csr-info csr                        Print info from certificate signing request
  csr-config-gen host                 Generate OpenSSL configuration file for certificate signing request generation
  crt-info crt                        Print info from certificate
┌ hpkp-gen csr backup                 Generate HTTP public key pinning (HPKP) header from CSR file
│ hpkp-gen key backup                 Generate HTTP public key pinning (HPKP) header from KEY file
└ hpkp-gen crt backup                 Generate HTTP public key pinning (HPKP) header from CRT file
┌ ocsp-gen server-cert issuer-cert    Generate OCSP stapling file from server certificate
└ ocsp-gen cert-chain                 Generate OCSP stapling file from server certificate chain
  ocsp-check host server-name         Check OCSP response status for some host
  0rtt-check host server-name         Check 0-RTT support
  htpasswd user password              Generate record with MD5 password hash for .htpasswd files

Options

  --ecc, -E        Generate ECC certificate signing request
  --size, -s size  Key size (ECC: 256-384 / RSA: 2048-8192)
  --help, -h       Show this help message
  --version, -v    Show information about version

Examples

  web-utils csr-gen domain.com
  Generate RSA key and a certificate signing request for domain.com

  web-utils hpkp-gen domain.com.csr domain.com.backup.key
  Generate HTTP public key pinning (HPKP) header with server and backup pins

  web-utils ocsp-gen sever.crt issuer.crt
  Generate OCSP stapling file using server and issuer certificates

  web-utils ocsp-gen sever-chain.crt
  Generate OCSP stapling file using certificate chain

  web-utils ocsp-check essentialkaos.com
  Check OCSP response status for essentialkaos.com
```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/web-utils/ci.svg?branch=master)](https://kaos.sh/w/web-utils/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/web-utils/ci.svg?branch=master)](https://kaos.sh/w/web-utils/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
