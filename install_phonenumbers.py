# install_phonenumbers.py

import subprocess
import sys

def install_phonenumbers():
    try:
        # Check if the module is already installed
        import phonenumbers
        print("phonenumbers module is already installed.")
    except ImportError:
        print("phonenumbers module is not installed. Installing...")

        # Install phonenumbers using pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'phonenumbers'])

        print("phonenumbers module has been successfully installed.")

if __name__ == "__main__":
    install_phonenumbers()

    # Prompt the user to press Enter before exiting
    input("Press Enter to exit...")
