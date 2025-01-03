# installs the correct version of python, creates a virtualenv, and installs requirements.

$install_python_path = "$($env:LOCALAPPDATA)\Programs\Python\Python312\python.exe"
$virtual_env_path = ".\starfield-console-cg-env"

if (-not(Test-Path -path $install_python_path)) {
    # If the python install doesn't exist, install it.
	Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe" -OutFile "$($env:HOMEPATH)\Downloads\python-3.12.8-amd64.exe"
	"$($env:HOMEPATH)\Downloads\python-3.12.8-amd64.exe InstallAllUsers=0 InstallLauncherAllUsers=0";
}


if (-not(Test-Path -path $virtual_env_path)) {
	# Create the Virtual Environment if it doesn't already exists
	$create_venv_command = "$install_python_path -m venv '$virtual_env_path'"
	Invoke-Expression $create_venv_command
}

# Activate the Virtual Environment and install requirements
Invoke-Expression "$virtual_env_path\Scripts\Activate.ps1"
Invoke-Expression "$virtual_env_path\Scripts\pip install -r ./requirements.txt"