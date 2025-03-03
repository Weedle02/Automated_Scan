# Automated Vulnerability Scanner Suite

A combined Python/Bash solution for scheduled vulnerability scanning with system automation and report management.

##  Components

### **Core Scanner** (`vuln_scanner.py`)
- Python-based scanning engine
- Features:
  - Nmap network scanning with CVE detection
  - Nikto web application checks
  - PDF report generation
  - Dynamic target input

### **System Manager** (cscan_manager.sh`)
- Bash automation wrapper
- Features:
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

##  Quick Start

1. Clone repository:
   git clone https://github.com/yourusername/vuln-scanner-suite.git
   cd vuln-scanner-suite
2. Install Python dependencies:
   pip install -r requirements.txt
3. Configure targets:
   echo "http://test-site.com" > targets.txt
4. Run full suite:
   ./scan_manager.sh 

## Security Note

   - Store targets.txt outside version control
   - Run with minimal privileges
   - Audit scan targets regularly
   - Use in compliance with all applicable laws
  
