# Windows Defender Analysis Script

## Overview

This repository contains a PowerShell script designed to analyze the status and health of Windows Defender on Windows 10/11 systems. The script is aimed at providing quick and useful insights into the current state of the built-in antivirus and any pending updates.

### Script Included

- **Analyze-WindowsDefender.ps1**
  - This script performs the following actions:
    - **Windows Defender Status Check:**
      - Displays whether Windows Defender is enabled.
      - Shows the status of Real-Time Protection.
      - Lists the current Antivirus Signature Version.
      - Indicates the last time a Quick Scan and Full Scan were performed.
    - **Checking for Regular Updates:**
      - Enumerates any pending Windows Updates that might be awaiting installation or restart.
    - **Windows Defender Health Check:**
      - Confirms whether Windows Defender's antivirus is enabled and real-time protection is active.
      - Verifies that the antivirus signatures are up to date.

  - **Note:** The script no longer outputs details regarding the last Defender update due to previous parsing issues and to streamline the output.

  - The script waits for the user to press "Enter" before exiting.
## 1. Script Description and User Instruction
  - The script starts with comments explaining its purpose and behavior:
  - Analyze-WindowsDefender.ps1
  - This script checks the status of Windows Defender, including its health, current status, and pending updates.
  - The script will not exit until the user presses "Enter".

## 2. Function to Ensure Administrative Privileges
  - This function, `Ensure-Admin`, checks if the script is running with administrator rights and restarts it with the required privileges if it's not.
  ![alt text](https://github.com/vaishnavucv/Project-winEvasion-Redteam/blob/main/Resource/FunctionEnsureAdministrativePrivileges.png?raw=true)

## 3. Main Execution - Checking Windows Defender Status

After ensuring the script runs with administrative privileges, it defines and invokes another function, `Get-DefenderStatus`, to fetch and display the status of Windows Defender.

![alt text](https://github.com/vaishnavucv/Project-winEvasion-Redteam/blob/main/Resource/MainExecutionCheckingWindowsDefenderStatus.png?raw=true)


### How to Use the Script

1. **Download the**  [script](https://github.com/vaishnavucv/Project-winEvasion-Redteam/blob/main/Project-Files/Analyze-WindowsDefender.ps1)
2. **RUn the script as Administrator** in poweshell


> ###Summary:
> - Ensure-Admin Function: Ensures the script is run with administrative privileges.
> - Get-DefenderStatus Function: Fetches and displays the status of Windows Defender, including the last quick scan and full scan details.