import os
import streamlit as st
import subprocess
from logging import getLogger


logger = getLogger(__name__)


# Si docker n'est pas lancé, on le lance # TODO: A retravailler pour une version multi-plateforme
if os.name == "nt":
    if b"Docker Desktop.exe" not in subprocess.check_output("tasklist"):
        if subprocess.run(r'"C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"') != 0:
            logger.fatal("Docker Desktop did not started, can't continue")
            exit()
        
else:
    raise OSError("OS type is currently not supported")
logger.debug("Docker engine started")

# ? Ce code est-il vraiment nécessaire ?
def init():
    keys = {
        "pages": None,
        "cookies_manager": None,
        "docker_warning_shown": False,
        "docker_warning": None,
        "run_docker": False,
        "account": None,
        "user": None,
        "messages": [],
    }

    for key, value in keys.items():
        if key not in st.session_state:
            st.session_state[key] = value
