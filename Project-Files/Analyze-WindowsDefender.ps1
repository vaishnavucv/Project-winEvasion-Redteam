# Analyze-WindowsDefender.ps1
# This script checks the status of Windows Defender, including its health, current status, and pending updates.
# The script will not exit until the user presses "Enter".

# Function to ensure script runs as administrator
function Ensure-Admin {
    if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
        Write-Host "The script needs to be run as an administrator." -ForegroundColor Red
        Start-Process powershell "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
        Exit
    }
}

# Call Ensure-Admin at the start
Ensure-Admin

function Get-DefenderStatus {
    Write-Host "`n==== Windows Defender Status ====" -ForegroundColor Cyan

    # Get Windows Defender status
    $status = Get-MpComputerStatus

    # Check Last Quick Scan and Last Full Scan status
    $lastQuickScan = if ($status.LastQuickScanEndTime) { $status.LastQuickScanEndTime } else { "No quick scan performed" }
    $lastFullScan = if ($status.LastFullScanEndTime) { $status.LastFullScanEndTime } else { "No full scan performed" }

    # Display the information in a tabular format
    $table = @"
    Status                                       Value
    -----------------------------------------------------
    Antivirus Enabled:                          $($status.AntivirusEnabled)
    Real-Time Protection Enabled:               $($status.RealTimeProtectionEnabled)
    Antivirus Signature Version:                $($status.AMProductVersion)
    Last Quick Scan:                            $lastQuickScan
    Last Full Scan:                             $lastFullScan
"@
    Write-Host $table -ForegroundColor Green
}

function Check-RegularUpdates {
    Write-Host "`n==== Checking for Regular Updates ====" -ForegroundColor Cyan
    
    # Using a simple check since Get-WindowsUpdate is not available
    $pendingUpdates = Get-WindowsUpdateLog | Select-String -Pattern "Pending Restart|Pending Install"

    if ($pendingUpdates) {
        Write-Host "Pending Updates:" -ForegroundColor Yellow
        $pendingUpdates | ForEach-Object {
            Write-Host $_.Line -ForegroundColor Yellow
        }
    } else {
        Write-Host "No pending updates." -ForegroundColor Green
    }
}

function Check-DefenderHealth {
    Write-Host "`n==== Windows Defender Health Check ====" -ForegroundColor Cyan

    $status = Get-MpComputerStatus

    # Check Antivirus Enabled
    if ($status.AntivirusEnabled) {
        Write-Host "Antivirus is enabled." -ForegroundColor Green
    } else {
        Write-Host "Antivirus is not enabled!" -ForegroundColor Red
    }

    # Check Real-Time Protection
    if ($status.RealTimeProtectionEnabled) {
        Write-Host "Real-Time Protection is enabled." -ForegroundColor Green
    } else {
        Write-Host "Real-Time Protection is not enabled!" -ForegroundColor Red
    }

    # Check if Signature is up to date
    $lastUpdate = $status.AntivirusSignatureLastUpdated

    if ($lastUpdate -ne $null -and $lastUpdate -ne "") {
        try {
            $lastUpdateDate = [datetime]::Parse($lastUpdate)
            $daysSinceLastUpdate = (Get-Date - $lastUpdateDate).Days

            if ($daysSinceLastUpdate -eq 0) {
                Write-Host "Antivirus signatures are up to date." -ForegroundColor Green
            } else {
                Write-Host "Antivirus signatures are out of date!" -ForegroundColor Red
            }
        } catch {
            # If there's an error parsing the date, we just don't report it
        }
    }
}

# Run the functions
Get-DefenderStatus
Check-RegularUpdates
Check-DefenderHealth

Write-Host "`nPress 'Enter' to exit the script..." -ForegroundColor Cyan
Read-Host
