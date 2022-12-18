import logging
from dynaconf import Dynaconf
import sys
from pathlib import Path
if sys.path[0][-3:] != 'HW3':
    sys.path[0] = str(Path(sys.path[0]).parent)

#Setting logging level
logging.basicConfig(level=logging.INFO)

#Setting Dynaconf
settings = Dynaconf(settings_file = "conf/settings.toml", envvar_prefix="DYNACONF", env_switcher="ENV_FOR_DYNACONF")

logging.info("Dynaconf settings created")
