import os
import sys
import json
import re
from getpass import getpass


HOMEDIR = os.getenv("HOME")
CONFIG_FILE = os.path.join(HOMEDIR, '.tracker_config.json')


def check_config(config=CONFIG_FILE):
    """
    Check the existence of configuration file

    Parameter
        config (str), optional:
            The file that contains user data. The default is CONFIG_FILE.

    Returns
        bool:
            Returns True if the file exist, returns false otherwise.
    """
    script_name = os.path.basename(sys.argv[0])
    if not os.path.isfile(CONFIG_FILE):
        print("Error: configuration file not found!")
        print(f"Please run '{script_name} intialize' first.")
        return None
    return True


def read_config(config=CONFIG_FILE):
    """
    Read the configuration file

    Parameter
        config (str), optional:
            The file that contains user data. The default is CONFIG_FILE.

    Returns
        data (dict):
            Dictionary that contains user data.
    """
    if check_config(config):
        with open(config) as f:
            data = json.load(f)
        return data
    return None


def safe_input(prompt, pattern):
    """
    Function that handles user input

    Parameters
        prompt (str):
            The message that is prompt to user.
        pattern (re.Pattern):
            the regex pattern to be used for matching.

    Returns
        userinput (str):
            A valid data entered by user.
    """
    while True:
        try:
            userinput = input(prompt)
        except KeyboardInterrupt:
            print()
            sys.exit(130)
        except EOFError:
            print()
            sys.exit(1)
        else:
            if re.match(pattern, userinput):
                break

    return userinput


def get_gmail():
    """
    Get the gmail address of user

    Returns
        gmail (str):
            The Gmail address of user.
    """
    pattern = re.compile(r'^\S+@gmail\.com(\.[a-z]{2})?$')
    prompt = 'Enter your Gmail: '
    gmail = safe_input(prompt, pattern)
    return gmail


def get_target_price():
    """
    Get the product price

    Returns
        target_price (float):
            A valid price entered by user.
    """
    pattern = re.compile(r'^\d+(\.\d+)?$')
    prompt = 'Enter your target price [should be greater than 0]: '
    target_price = float(safe_input(prompt, pattern))
    if target_price <= 0:
        return get_target_price()
    else:
        return target_price


def get_product_url():
    """
    Get the Amazon product url

    Returns
        product_url (str):
            A valid url of the product entered by user.
    """
    pattern = re.compile(r'^(https?://)?www.amazon.com(\.[a-z]{2})?/\S+')
    prompt = 'Enter Amazon product url: '
    product_url = safe_input(prompt, pattern)
    return product_url


def initialize(config=CONFIG_FILE):
    """
    Initialize the configuration file

    Parameters
        config (str), optional:
            The file that contains user data. The default is CONFIG_FILE.
    """
    data = dict()
    data['gmail'] = get_gmail()
    data['password'] = getpass('Enter password: ')
    data['url'] = get_product_url()
    data['target_price'] = get_target_price()

    with open(config, 'w') as f:
        json.dump(data, f, indent=4)
