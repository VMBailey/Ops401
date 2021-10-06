# Script Name:                     Automating Workstation Configuration
# Author:                          Vincent Bailey
# Date of Latest Revision:         10/4/2021
# Purpose:                         This script will lock the user's workstation, run a full Windows
#                                  Defender scan, and then run and install any new updates.


# This line will lock the screen.
rundll32.exe user32.dll,LockWorkStation

# These lines will check the status of Windows Defender and initiate a full scan.
Get-MpComputerStatus
Update-MpSignature
Start-MpScan -ScanType FullScan

# This line will initiate Windows Updates, install them automatically, and then reboot the computer.
Get-WindowsUpdate -AcceptAll -Install -AutoReboot