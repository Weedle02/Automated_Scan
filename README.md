# Automated Vulnerability Scanner

A Python script that performs scheduled network and web application vulnerability scans using open-source tools. Generates consolidated PDF reports from scan results.

## Tools Required
- **Nmap** (7.80+) with Vulners script (for network/CVE scanning)
- **Nikto** (2.1.6+) (for web application scanning)
- Python 3.6+ with `reportlab` package

## Features
- Dynamic target input (IPs/URLs) via `targets.txt`
- Scheduled daily scans (24-hour interval)
- Consolidated PDF reporting
- Automatic result categorization
- Network and web app scanning integration

## Usage
 - python3 vuln_scanner.py
 - Reports generated in /reports directory
 - Format: vulnerability_report_TIMESTAMP.pdf

## Disclamer
 - Use only on authorized systems. The maintainers are not responsible for misuse of this tool.

WIP
