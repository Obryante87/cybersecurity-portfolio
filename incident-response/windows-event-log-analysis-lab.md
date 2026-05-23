# Windows Event Log Analysis Lab

## Objective

The objective of this lab was to review Windows event logs for signs of suspicious authentication activity, failed login attempts, privilege use, and possible persistence indicators.

## Tools Used

- Windows Event Viewer
- Windows Security Logs
- PowerShell
- Sysmon
- MITRE ATT&CK Framework

## Environment

This lab was performed in a Windows test environment. The focus was on reviewing common Windows event IDs that are useful during incident response and security monitoring.

## Key Event IDs Reviewed

| Event ID | Description | Security Relevance |
|---|---|---|
| 4624 | Successful logon | Helps identify valid account access |
| 4625 | Failed logon | Helps identify brute-force attempts or unauthorized access attempts |
| 4672 | Special privileges assigned | May indicate privileged account activity |
| 4688 | Process creation | Useful for reviewing suspicious processes |
| 7045 | New service installed | May indicate persistence through service creation |

## Steps Performed

1. Opened Windows Event Viewer.
2. Navigated to Windows Logs.
3. Reviewed Security logs for authentication events.
4. Filtered for failed logon attempts using Event ID 4625.
5. Reviewed successful logons using Event ID 4624.
6. Checked for privileged logons using Event ID 4672.
7. Reviewed process creation activity where available.
8. Documented findings and security relevance.

## Findings

During the review, failed logon events can help identify possible password guessing, brute-force attempts, or misconfigured services. Successful logon events help establish whether access occurred and what account was used. Privileged logon events are especially important because they may show administrative access.

## Security Relevance

Windows event logs are an important source of evidence during incident response. Reviewing authentication activity, privilege use, and service creation can help identify suspicious behavior, account misuse, and possible persistence mechanisms.

## Lessons Learned

This lab reinforced the importance of knowing common Windows event IDs and understanding how authentication activity appears in system logs. It also showed how basic log review can support incident response and threat hunting.
