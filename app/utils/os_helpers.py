# app/utils/os_helpers.py
import os
import subprocess
import platform

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def get_os_type():
    return platform.system()
