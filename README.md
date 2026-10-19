# NetAudit

[![ci](https://github.com/BebinTailan/NetAudit/actions/workflows/ci.yml/badge.svg)](https://github.com/BebinTailan/NetAudit/actions/workflows/ci.yml)

NetAudit inventories a network you are responsible for: it discovers live hosts, finds open TCP
services, identifies them from their banners and flags exposed or outdated services, then produces
a report you can compare over time. It uses Python's `asyncio` and the standard library only.

> **Status:** early development. See [docs/ROADMAP.md](docs/ROADMAP.md).

## Authorized use only

Only scan systems you own or have **written permission** to assess. NetAudit refuses public IP
ranges unless explicitly allowed, rate-limits itself, and records the scope of every run in its report.

## Requirements

- Python 3.11+
- No third-party dependency

## Usage

```bash
python -m netaudit --version
```

## Development

```bash
python -m unittest discover -s tests -v
```

Tests only use local servers on `127.0.0.1`; they never scan a real network.
