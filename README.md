# Cybersecurity Portfolio

This repository documents my hands-on cybersecurity learning and project work. The purpose of this portfolio is to demonstrate practical skills in security operations, incident response, networking, Linux administration, vulnerability management, and technical documentation.

## Portfolio Areas

| Area | Description |
|---|---|
| SIEM & Detection Engineering | Microsoft Sentinel, Defender XDR, KQL detection development, analytics rules, alerting, and incident investigation |
| Incident Response | Labs focused on log analysis, authentication review, persistence, and investigation notes |
| Networking | Packet analysis, TCP/IP review, DNS analysis, and Wireshark labs |
| Linux Security | Linux hardening, permissions, firewall configuration, and SSH security |
| Vulnerability Management | Vulnerability scanning, risk prioritization, and remediation planning |
| Python Security Tools | Small scripts for automation, parsing logs, hashing files, and basic security tasks |
| Security Documentation | Templates for policies, incident reports, risk registers, and technical summaries |

## Project Format

Each project includes:

- Objective
- Tools used
- Lab environment
- Steps performed
- Findings
- Security relevance
- Lessons learned

## Featured Projects

### Microsoft Sentinel SIEM Detection Engineering Lab

Built an end-to-end SIEM detection and investigation lab using Microsoft Sentinel, Microsoft Defender XDR, Windows security telemetry, and Kusto Query Language (KQL).

The lab demonstrates the complete detection lifecycle:

**Windows Endpoint → Event Logging → Log Analytics → Microsoft Sentinel → KQL Detection → Analytics Rule → Defender XDR Alert → Incident Investigation**

Key work completed:
- Collected Windows PowerShell and Security event telemetry
- Developed KQL detections for PowerShell Script Block Logging (Event ID 4104)
- Investigated Windows process creation events (Event ID 4688)
- Correlated authentication activity using Event ID 4624 and Logon IDs
- Reconstructed parent/child process execution chains
- Created a scheduled Microsoft Sentinel analytics rule
- Generated and validated alerts in Microsoft Defender XDR
- Confirmed incident creation through the `SecurityIncident` table
- Documented investigation evidence with screenshots and reusable KQL queries

**[View the Microsoft Sentinel SIEM Detection Engineering Lab](siem-detection-engineering/)**

---

### Additional Projects

1. [Windows Event Log Analysis Lab](incident-response/)
2. [Linux Hardening Lab](linux-security/)
3. [Wireshark Network Traffic Analysis](networking/)
4. [Vulnerability Management Lab](vulnerability-management/)
5. [Python Security Tools](python-security-tools/)

## About Me

I am a cybersecurity and information systems professional with experience in network operations, information assurance, incident response support, cyber hygiene, and technical documentation. I am currently expanding my skills in Linux, networking, security operations, and cybersecurity automation.
