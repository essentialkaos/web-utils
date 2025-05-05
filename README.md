<p align="center"><a href="#readme"><img src=".github/images/card.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/web-utils/ci"><img src="https://kaos.sh/w/web-utils/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src=".github/images/license.svg"/></a>
</p>

<p align="center"><a href="#installation">Installation</a> • <a href="#usage">Usage</a> • <a href="#ci-status">CI Status</a> • <a href="#license">License</a></p>

<br/>

`web-utils` is helpers for working with web server.

### Installation

#### From [ESSENTIAL KAOS Public Repository](https://kaos.sh/kaos-repo)

```
sudo dnf install -y https://pkgs.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo dnf install web-utils
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

<img src=".github/images/usage.svg" />

### CI Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/web-utils/ci.svg?branch=master)](https://kaos.sh/w/web-utils/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/web-utils/ci.svg?branch=master)](https://kaos.sh/w/web-utils/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://kaos.dev"><img src="https://raw.githubusercontent.com/essentialkaos/.github/refs/heads/master/images/ekgh.svg"/></a></p>
