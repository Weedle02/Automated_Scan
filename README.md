# Automated Vulnerability Scanner Suite

A combined Python/Bash solution for scheduled vulnerability scanning with system automation and report management.

##  Components

### **Core Scanner** (`vuln_scanner.py`)
- Python-based scanning engine
  - Nmap network scanning with CVE detection
  - Nikto web application checks
  - PDF report generation
  - Dynamic target input

### **System Manager** (`scan_manager.sh`)
- Bash automation wrapper
  - Pre-flight dependency checks
  - Report rotation/archiving
  - Scan scheduling integration
  - System resource validation

## Requirements

| Component      | Version | Note                          |
|----------------|---------|-------------------------------|
| Python         | 3.6+    | Requires `reportlab` package  |
| Nmap           | 7.80+   | With Vulners script           |
| Nikto          | 2.1.6+  |                               |
| Bash           | 4.4+    | For advanced features         |
| Make (optional)| 4.2+    | For build automation          |


## Security Note

   - Store `targets.txt` outside version control
   - Run with minimal privileges
   - Audit scan targets regularly
   - Use in compliance with all applicable laws

WIP
  
