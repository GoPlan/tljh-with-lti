## file: jupyterhub_config_lti11.py ##
""" Example JupyterHub configuration file with LTI 1.1 settings. """
import os
import sys

# (dar) this is a hack
sys.path.append("/usr/local/lib/python3.8/dist-packages")
import ltiauthenticator

# Set log level
c.Application.log_level = "DEBUG"

# Set the LTI 1.1 authenticator.
c.JupyterHub.authenticator_class = "ltiauthenticator.LTIAuthenticator"

# # Add the LTI 1.1 consumer key and shared secret. Note the use of
# # `LTI11Authenticator` vs the legacy `LTIAuthenticator`.
# c.LTI11Authenticator.consumers = {
#     os.environ["LTI_CLIENT_KEY"]: os.environ["LTI_SHARED_SECRET"]
# }

# (dar) the key&secret should not be hard coded.
# for some reason python is not seeing the docker ENV VARS.

LTI_CLIENT_KEY = "0c676cd363e7fdb18c3a855eec8ab180213af6c201733bc14ab50c4f37c74b29"
LTI_SHARED_SECRET = "0f41e00085b3f411ea5ebb4093c37b56f2bce67bd00bf4a69dffbef2c09bf244"
c.LTI11Authenticator.consumers = { LTI_CLIENT_KEY : LTI_SHARED_SECRET }

# Use an LTI 1.1 parameter to set the username.
c.LTI11Authenticator.username_key = "lis_person_name_full"
