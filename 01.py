import subprocess

def check_bluetooth_connected():
    try:
        # Use PowerShell command to list connected Bluetooth devices
        command = 'powershell "Get-PnpDevice -Class Bluetooth | Where-Object { $_.Status -eq \'OK\' }"'
        result = subprocess.check_output(command, shell=True, text=True)

        if result.strip():
            print("Connected Bluetooth Devices:")
            print(result)
        else:
            print("No Bluetooth devices are currently connected.")
    except Exception as e:
        print(f"Error: {e}")

check_bluetooth_connected()
