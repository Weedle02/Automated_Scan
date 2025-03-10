#!/usr/bin/env python3
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
import os
from time import sleep
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

TARGETS_FILE = "/path/to/targets.txt"
REPORTS_DIR = "/path/to/reports"
SCAN_INTERVAL = 86400  

def create_directories():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def load_targets():
    with open(TARGETS_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def run_nmap(ip):
    filename = f"nmap_scan_{ip.replace('/', '_')}.xml"
    command = [
        "nmap",
        "-v",
        "-sV",
        "--script=vulners",
        "-oX",
        os.path.join(REPORTS_DIR, filename),
        ip
    ]
    subprocess.run(command, check=True)
    return filename

def run_nikto(url):
    filename = f"nikto_scan_{url.replace('://', '_').replace('/', '_')}.xml"
    command = [
        "nikto",
        "-h",
        url,
        "-Format",
        "XML",
        "-o",
        os.path.join(REPORTS_DIR, filename)
    ]
    subprocess.run(command, check=True)
    return filename

def parse_nmap_results(xml_file):
    results = []
    tree = ET.parse(os.path.join(REPORTS_DIR, xml_file))
    root = tree.getroot()
    
    for host in root.findall('host'):
        ip = host.find('address').get('addr')
        for port in host.findall('ports/port'):
            port_id = port.get('portid')
            service = port.find('service').get('name')
            product = port.find('service').get('product', '')
            version = port.find('service').get('version', '')
            results.append(f"IP: {ip} | Port: {port_id} | Service: {service} {product} {version}")
    return results

def parse_nikto_results(xml_file):
    results = []
    tree = ET.parse(os.path.join(REPORTS_DIR, xml_file))
    root = tree.getroot()
    
    for item in root.findall('scandetails/item'):
        description = item.find('description').text
        results.append(description)
    return results

def generate_pdf_report():
    styles = getSampleStyleSheet()
    report_file = os.path.join(REPORTS_DIR, f"vulnerability_report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf")
    doc = SimpleDocTemplate(report_file, pagesize=letter)
    story = []
    
    story.append(Paragraph("Vulnerability Scan Report", styles['Title']))
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Network Scan Results (Nmap):", styles['Heading2']))
    for file in os.listdir(REPORTS_DIR):
        if file.startswith('nmap_scan'):
            results = parse_nmap_results(file)
            for line in results:
                story.append(Paragraph(line, styles['BodyText']))
                story.append(Spacer(1, 5))
    
    story.append(PageBreak())
    
    story.append(Paragraph("Web Application Scan Results (Nikto):", styles['Heading2']))
    for file in os.listdir(REPORTS_DIR):
        if file.startswith('nikto_scan'):
            results = parse_nikto_results(file)
            for line in results:
                story.append(Paragraph(line, styles['BodyText']))
                story.append(Spacer(1, 5))
    
    doc.build(story)

def main():
    create_directories()
    while True:
        targets = load_targets()
        nmap_files = []
        nikto_files = []
        
        for target in targets:
            try:
                if target.startswith('http'):
                    nikto_files.append(run_nikto(target))
                else:
                    nmap_files.append(run_nmap(target))
            except subprocess.CalledProcessError as e:
                print(f"Error scanning {target}: {str(e)}")
        
        generate_pdf_report()
        print(f"Scan completed. Report generated in {REPORTS_DIR}")
        sleep(SCAN_INTERVAL)

if __name__ == "__main__":
    main()
