# Windows: Machine

## Add new Python environment
python -m venv venv

# Optional resolve PowerShell execution policy restriction
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

## Activate Python environment before starting work
venv\Scripts\activate

## Install required packages
pip install -r requirements.txt
## Deactivate Python environment
deactivate
## Delete or remove Python env
rmdir /s /q venv



# Mac or Linux:



## Add new Python environment
python3 -m venv ./venv

## Activate Python environment before starting work

source ./venv/bin/activate

## Check if environment is successfully activated or not
which python3

## Install required packages
pip3 install -r requirements.txt

## Deactivate Python environment
deactivate

## Delete or remove Python env 
rm -rf ./venv
