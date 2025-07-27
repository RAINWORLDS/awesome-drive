# backend/main.py
import webbrowser
import uvicorn
import threading

def start_server():
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)

if __name__ == "__main__":
    threading.Thread(target=start_server).start()
    webbrowser.open("http://127.0.0.1:8000")
