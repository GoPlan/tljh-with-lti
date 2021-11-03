# The Littlest JupyterHub with LTI 

This project is meant to be used to getting up and running with
jupyterhub as an LTI v1.1 tool provider for and openedx studio as an
LTI consumer.

## Prerequisites

tested with 

- docker version 20.10.10, build b485636
- docker-compose version 1.29.2, build 5becea4c

## Getting started 

The following command should produce a running of instance of
jupyterhub on port 12000 with LTI configured.

    $ make build && make up && make firstrun    
    
## TODO

- The LTI consumer key & shared secret are both hard coded at the
  moment, those need to be change and should be managed securely.
  
- src/jupyterhub_config_lti11.py is also using the hard coded
  key/secret although the issue causing that may have been resolved
  with the move to docker-compose.

