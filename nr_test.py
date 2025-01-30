from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
from dotenv import load_dotenv
import os
from time import time

load_dotenv(verbose=True)
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

def init_nornir():
    """
    Initialize Nornir object
    """
    nr = InitNornir(config_file="config.yml")
    nr.inventory.defaults.username = username
    nr.inventory.defaults.password = password
    return nr


def main():
    nr = init_nornir()
    starting_time = time()
    result = nr.run(
        task=send_command,
        command="show chassis hardware"
    )
    print_result(result) 
    print ('\n---- End elapsed time=', time() - starting_time)

if __name__ == "__main__":
    main()
