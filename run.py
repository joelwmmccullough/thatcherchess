"""
    run.py. it runs it

    python run.py                           # desktop window
    python run.py --browser                 # opens in default browser
    python run.py --browser --no-open       # starts server only; prints URL

"""

import argparse
import threading
import time
import webbrowser

import uvicorn

from thatcherchess.server import app

HOST = "127.0.0.1"
PORT = 8765


def start_server() -> None:
    """Wake up uvicorn"""
    config = uvicorn.Config(app, host=HOST, port=PORT, log_level="warning")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    time.sleep(1.0)


def wait_for_ctrl_c() -> None:
    """keep prog alive until u ctrl-c"""
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down server...")


def main() -> None:
    parser = argparse.ArgumentParser(description="run ThatcherChess.")
    parser.add_argument("--browser", action="store_true", help="open in default browser")
    parser.add_argument("--no-open", action="store_true", help="start server only; prints URL")
    args = parser.parse_args()

    start_server()
    url = f"http://{HOST}:{PORT}/api/ping"
    print(f"ThatcherChess is running at {url}")

    if args.no_open:
        wait_for_ctrl_c()
    elif args.browser:
        webbrowser.open(url)
        wait_for_ctrl_c()
    else:
        # pywebview is only needed for window not --browser and --no-open, so it is imported here
        import webview

        webview.create_window("ThatcherChess", url, width=1180, height=820)
        webview.start()


if __name__ == "__main__":
    main()