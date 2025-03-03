#!/bin/bash

verify_tools() {
    command -v nmap >/dev/null 2>&1 || { echo "Error: nmap not installed"; exit 1; }
    command -v nikto >/dev/null 2>&1 || { echo "Error: nikto not installed"; exit 1; }
}

rotate_reports() {
    find reports/ -name "*.pdf" -mtime +7 -exec gzip {} \;
}

verify_tools
python3 vuln_scanner.py
rotate_reports
