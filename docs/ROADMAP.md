# Roadmap

Each feature is developed on its own branch (`feature/NN-slug`) and merged into `main` when complete.

## Milestone v0.2.0: safe scanning core

- [ ] **01 scope-and-safety**: target parsing (IPs, CIDR, ranges, hostnames), private-range guard, explicit `--allow-public` opt-in, maximum target count, scope recorded in results
- [ ] **02 tcp-connect-scanner**: asyncio connect scan with concurrency limit, per-connection timeout, global rate limit and port lists (`top`, ranges, lists)
- [ ] **03 host-discovery**: TCP "ping" on common ports, with results cached per run

## Milestone v0.3.0: identification

- [ ] **04 banner-grabbing**: protocol-aware probes (SSH, HTTP, FTP, SMTP, generic) with byte and time limits
- [ ] **05 service-fingerprints**: signature rules to identify product and version from banners
- [ ] **06 exposure-rules**: rules file (JSON) flagging risky exposures (Telnet, SMB, RDP on unexpected hosts) and outdated versions, each rule citing its public source

## Milestone v1.0.0: reporting

- [ ] **07 reports**: JSON, CSV and HTML reports with scope, timing and findings
- [ ] **08 scan-diff**: compare two runs (new or closed ports, new hosts, changed versions)
- [ ] **09 config-and-cli**: TOML configuration profiles, `netaudit scan` / `netaudit diff`, exit codes for CI use
