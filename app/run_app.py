import subprocess
import time

def run_flask():
    print("Starting Flask backend...")
    flask_process = subprocess.Popen(["python", "main.py"])
    return flask_process

def run_streamlit():
    print("Starting streamlit frontend...")
    streamlit_process = subprocess.Popen(["streamlit", "run", "streamlit_frontend.py"])
    return streamlit_process

if __name__ == "__main__":
    flask_process = run_flask()

    time.sleep(10)

    streamlit_process = run_streamlit()

    try:
        flask_process.wait()
        streamlit_process.wait()
    except KeyboardInterrupt:
        print("Shutting down both processes:")
        flask_process.terminate()
        streamlit_process.terminate()