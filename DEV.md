# ALL THINGS DEVELOPMENT

## DEVELOPMENT

## GETTING STARTED

This project is currently using zephyr.
It is necessary you have installed:
- python > 3.10
- CMake > 3.20.5
- Devicetree-Compiler > 1.4.6

You can find all necessary dependencies and how to install them in [the zephyr wiki](https://docs.zephyrproject.org/latest/develop/getting_started/index.html).

There is an automatic installer script that you can run via: 
```bash
python3 auto_install.py
```
(_I DON'T RECOMMEND RUNNING RANDOM PYTHON SCRIPTS OF PEOPLE YOU DON'T KNOW WITHOUT CHECKING THEM FIRST_
All this script does is install the required packages and activate a python venv. Never the less make it a habit to never blindly run of code unknown source on your machine)

For more in-depth information on how to install all of these visit [the zephyr wiki](https://docs.zephyrproject.org/latest/develop/getting_started/index.html).

### West & Zephyr 
Developing for zephyr need the zephyr source code checked out, but not inside the git repository you are working in. For more information about this have a look at [the zephyr wiki](https://docs.zephyrproject.org/latest/develop/getting_started/index.html).


### PYTHON
Activate the python environment via:
```bash
source ~/.venv/bin/activate
```


