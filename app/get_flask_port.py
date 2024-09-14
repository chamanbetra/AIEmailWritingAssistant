import time

def get_flask_port(port_file="flask_port.txt", retries=5, delay=1):
    for i in range(retries):
        try:
            with open(port_file, "r") as f:
                flask_port = f.read().strip()
                if flask_port:
                    return flask_port
        except FileNotFoundError:
            print(f"Flask port file '{port_file}' not found. Retrying... ({i + 1}/{retries})")

        time.sleep(delay)
    
    print(f"Failed to retrieve Flask port after {retries} retries.")
    return None
    
