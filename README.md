# Project-winEvasion-Redteam
#### This Project is build for [Joyel](https://github.com/joyelpbiju) and  [Joshua](https://github.com/JOSHUAPBIJU) Master Applied Computer Science (MACS) students from [Hochschule Schmalkalden - University of Applied Sciences](https://www.hs-schmalkalden.de/en/) Germany 
### Course: Advanced Tactics in Information Security 

> [!NOTE]
> This project integrates the MITRE ATT&CK framework with advanced red team tactics to identify and exploit security vulnerabilities in Windows systems.

> [!TIP]
> Use PowerShell scripts with advanced obfuscation techniques to create Fully Undetectable (FUD) payloads that can bypass Windows Defender.

> [!IMPORTANT]
> Regular updates to FUD payloads are necessary to keep up with the latest Windows security features and ensure continued effectiveness.

> [!WARNING]
> Simulated attacks in this project reveal potential vulnerabilities that adversaries might exploit, emphasizing the need for robust cybersecurity measures.

> [!CAUTION]
> This project demonstrates sophisticated cyber-attacks, and its findings should be used responsibly to enhance defensive strategies and improve system security.

### Scenario :
**An adversary attempts to send a _phishing email_ to technical support _employees of a XYZ company_ . One of the employees, who lacks cybersecurity knowledge, opens the email and downloads an attached file. The file is a password-protected ZIP archive. The employee manages to unzip the file and install or test the content within it.
Meanwhile, the adversary gains access to the employee's company laptop. The adversary delivers a PowerShell script disguised as an executable (EXE) file. This script downloads a PowerShell script (PS1) from a cloud server into memory and executes it, bypassing detection by the employee and the default Windows security mechanisms.
The PowerShell script is obfuscated to evade antivirus detection. Once the obfuscated script is running in memory, it gains access to the laptop and spams UAC (User Account Control) prompts to obtain administrative rights. After successfully bypassing UAC, the adversary gains full control over the system.** 


> [!NOTE]
> **Bāsed on this scenario, the relevant MITRE ATT&CK® techniques are as follows:**
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
> [!NOTE]
> ATT&CK Navigator File
[Attack json file | download ](https://raw.githubusercontent.com/vaishnavucv/Project-winEvasion-Redteam/main/Resource/adversary_tactics_and_techniques_for_hacking_win11-10_using_phishing_scenario.json) upload to [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) for customization or for better view.

+ MITRE ATT&CK®
![MITRE ATT&CK®](https://raw.githubusercontent.com/vaishnavucv/Project-winEvasion-Redteam/d964b8e74194f45dbec1982d6abb2ab59e2c0ec2/Resource/Adversary_Tactics_and_Techniques_for_Phishing_Scenario(3).svg)

- [x] The above attack can be improvised 
- [ ] Effort calculated:- 100 hours 🕙 in 2.5 months 📆 [on-going porject] 	`Approximate value`
- [ ] Add delight to the experience when all tasks are completed


### **References**

  1. [scenario reference-01](https://www.techopedia.com/antivirus/antivirus-statistics)
  2. [scenario reference-02](https://www.malwarebytes.com/blog/news/2020/10/work-devices-for-personal-use)
  3. [MITRE ATT&CK®](https://attack.mitre.org/)
  4. [Attack-Naigator](https://mitre-attack.github.io/attack-navigator/)
  5. [Windows 10/11 security update](https://techcommunity.microsoft.com/t5/windows-servicing/updates-so-often/m-p/39526)

#### **update coming soon..!**
