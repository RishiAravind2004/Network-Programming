# Network-Programming (Simple TCP Server)
A example python program to communicate between server and client, This project demonstrates a simple TCP server in Python that listens for incoming connections, receives a message from the client, and sends a response back to the client.

## Getting Started

These instructions will guide you through the process of running the TCP server on your machine & client.

### Prerequisites

You need to have Python installed on your machine. You can download and install Python from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/RishiAravind2004/Network-Programming.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Network-Programming
    ```

    Or

Simply Download both server() and client() files.

### Running the Server

1. Open a terminal window.

2. Run the server script:

    ```bash
    python server.py
    ```

The server will start and listen for incoming connections on the specified IP address and port.

### Configuration

By default, the server is configured to listen on the IP address `192.168.1.43` and port `12345`. You can change these values in the `server.py` file by modifying the following lines:

```python
if __name__ == "__main__":
    host = '192.168.1.43'  # Change this to your desired IP address
    port = 12345           # Change this to your desired port
    start_server(host, port)
