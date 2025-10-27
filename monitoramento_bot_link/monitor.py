import requests
from config import URL_MONITOR

def checar_link():
    try:
        r = requests.get(URL_MONITOR, timeout=5)
        return r.status_code == 200
    except Exception:
        return False
