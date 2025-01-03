$virtual_env_path = ".\starfield-console-cg-env"
$install_python_path = "$($env:LOCALAPPDATA)\Programs\Python\Python312\python.exe"

if (-not(Test-Path -path $virtual_env_path) -Or -not(Test-Path -path $install_python_path)) {
    # If the virtual environment isn't setup, install the needed files.
    Write-Output "------------------------------------------------------------------------"
    Write-Output "The needed Python install and/or the virtual environment is not set up."
    Write-Output "We need to run an additional script to create them."
    Write-Output "------------------------------------------------------------------------"
    &./install_prereqs.ps1
} else {
    # If the virtual environment is setup, activate the virtual environment.
    Invoke-Expression "$virtual_env_path\Scripts\Activate.ps1"
}

Invoke-Expression "$virtual_env_path\Scripts\python.exe -m starfieldccg"
# &python -m starfieldccg

pause