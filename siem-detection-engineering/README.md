# SIEM & Detection Engineering

This section documents hands-on security monitoring, detection engineering, and incident investigation projects using Microsoft Sentinel, Microsoft Defender XDR, Windows security telemetry, and Kusto Query Language (KQL).

The goal of these labs is to demonstrate the complete detection lifecycle:

**Telemetry Collection → Detection Logic → Alert Generation → Incident Creation → Investigation → Triage → Documentation**

---

## Microsoft Sentinel SIEM Lab

### Overview

I built a Microsoft Sentinel SIEM lab to collect Windows security telemetry, develop custom KQL detections, generate security alerts and incidents, and investigate suspicious activity using Microsoft Sentinel and Microsoft Defender XDR.

The lab uses a Windows endpoint (`win-siem-01`) as the monitored system and a Log Analytics workspace connected to Microsoft Sentinel.

### Lab Architecture

```text
Windows Endpoint (win-siem-01)
        |
        v
Windows Event Logging
        |
        v
Azure Monitor / Log Analytics
        |
        v
Microsoft Sentinel
        |
        v
Scheduled Analytics Rule
        |
        v
Microsoft Defender XDR
        |
        v
Alert / Incident Investigation
