![MITRE ATT&CK®](https://attack.mitre.org/theme/images/ATT&CK_red.png)
### What is MITRE ATT&CK® .?

**MITRE ATT&CK®** is a comprehensive framework that maps out the tactics, techniques, and procedures (TTPs) used by cyber adversaries. It provides a detailed matrix to understand and simulate real-world attack scenarios. This helps organizations to identify vulnerabilities and strengthen their defenses. By using MITRE ATT&CK®, security professionals can better anticipate and mitigate potential threats.

**Bāsed on this scenario in [main-readme.md file](https://github.com/vaishnavucv/Project-winEvasion-Redteam/blob/main/README.md), the relevant MITRE ATT&CK® techniques are as follows:**
1. Phishing Email Sent to Employee
    -	Technique: Phishing
    - Tactic: Initial Access
    - ID: T1566
2.	Employee Opens and Downloads the File
    - Technique: User Execution
    - Tactic: Execution
    - ID: T1204
3.	File is a ZIP with Password
    - Technique: Archive Collected Data
    - Tactic: Collection
    - ID: T1560
4.	Employee Unzips and Tests the File
    - Technique: User Execution
    - Tactic: Execution
    - ID: T1204
5.	Adversary Gains Access to the Laptop
    - Technique: Valid Accounts
    - Tactic: Persistence
    - ID: T1078
6.	PowerShell Script Delivered as EXE
    - Technique: Command and Scripting Interpreter: PowerShell
    - Tactic: Execution
    - ID: T1059.001
7.	PowerShell Script Downloads and Executes in Memory
    - Technique: Ingress Tool Transfer
    - Tactic: Command and Control
    - ID: T1105
8.	Script Obfuscation to Avoid Detection
    - Technique: Obfuscated Files or Information
    - Tactic: Defense Evasion
    - ID: T1027
9.	Spamming UAC Prompts to Gain Admin Rights
    - Technique: Bypass User Account Control
    - Tactic: Privilege Escalation
    - ID: T1548.002
