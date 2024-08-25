## Script to Payload.exe

### To install PS2EXE on Windows 11, follow these steps:

1. **Open PowerShell as Administrator:**
   - Right-click the Start menu and select "Windows PowerShell (Admin)" or "PowerShell (Admin)".

2. **Install the PS2EXE module:**
   - In the PowerShell window, run the following command to install the PS2EXE module from the PowerShell Gallery:
   ```powershell
   Install-Module -Name PS2EXE -Scope CurrentUser -Force
> If prompted to install the NuGet provider, type Y and press Enter.
3. Verify Installation:

    Run the following command to ensure PS2EXE is installed correctly:
    ```powershell
    Get-Command -Module PS2EXE
    ```
4. Convert the PowerShell script to an executable (.exe):

    You can use the GUI of the PS2EXE application located at:
    ```powershell
    C:\Program Files\WindowsPowerShell\Modules\ps2exe\1.0.13
    ```
    > Fill in the required information in the PS2EXE application and start the conversion.
    #
   ![alt text](https://raw.githubusercontent.com/vaishnavucv/Project-winEvasion-Redteam/main/Resource/PS2EXE.png)

5. Important Notes:

    While converting, the name and icon of the executable are crucial and should be carefully chosen.