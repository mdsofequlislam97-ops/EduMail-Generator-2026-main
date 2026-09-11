import sys
import subprocess
import os

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

def get_chrome_version():
    """
    Get installed Chrome browser version.
    Returns version string or None if not found.
    """
    try:
        if sys.platform == 'win32':
            # Windows
            result = subprocess.check_output(
                'powershell "(Get-Item \'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\').VersionInfo.ProductVersion"',
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip()
        elif sys.platform == 'darwin':
            # macOS
            result = subprocess.check_output(
                '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version',
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip().split()[-1]
        else:
            # Linux
            result = subprocess.check_output(
                'google-chrome --version',
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip().split()[-1]
        return result
    except:
        return None

def get_firefox_version():
    """
    Get installed Firefox browser version.
    Returns version string or None if not found.
    """
    try:
        if sys.platform == 'win32':
            # Windows
            result = subprocess.check_output(
                'powershell "(Get-Item \'C:\\Program Files\\Mozilla Firefox\\firefox.exe\').VersionInfo.ProductVersion"',
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip()
        elif sys.platform == 'darwin':
            # macOS
            result = subprocess.check_output(
                '/Applications/Firefox.app/Contents/MacOS/firefox --version',
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip().split()[-1]
        else:
            # Linux
            result = subprocess.check_output(
                'firefox --version',
                shell=True,
                stderr=subprocess.DEVNULL
            ).decode('utf-8').strip().split()[-1]
        return result
    except:
        return None

def setup_chrome_driver():
    """
    Setup Chrome WebDriver using webdriver-manager.
    Automatically downloads and manages ChromeDriver.
    """
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        ChromeDriverManager().install()
        return True
    except Exception as e:
        print(f"Error setting up Chrome WebDriver: {str(e)}")
        return False

def setup_firefox_driver():
    """
    Setup Firefox WebDriver using webdriver-manager.
    Automatically downloads and manages GeckoDriver.
    """
    try:
        from webdriver_manager.firefox import GeckoDriverManager
        GeckoDriverManager().install()
        return True
    except Exception as e:
        print(f"Error setting up Firefox WebDriver: {str(e)}")
        return False
