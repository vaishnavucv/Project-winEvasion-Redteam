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

### How to Use the Script

1. **Download the**  [script](https://github.com/vaishnavucv/Project-winEvasion-Redteam/blob/main/Project-Files/Analyze-WindowsDefender.ps1)
2. **RUn the script as Administrator** in poweshell

