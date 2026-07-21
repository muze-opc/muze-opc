from datetime import datetime


def _time():
    return datetime.now().strftime("%H:%M:%S")


def info(message):
    print(f"[{_time()}] INFO     {message}")


def success(message):
    print(f"[{_time()}] SUCCESS  {message}")


def warning(message):
    print(f"[{_time()}] WARNING  {message}")


def error(message):
    print(f"[{_time()}] ERROR    {message}")