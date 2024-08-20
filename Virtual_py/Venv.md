# Virtual Enviroment in Python

## - We need a virtual enviroment for python bcoz it helps to install all package for python virtually so that the main machine dont need to be flooded with python packages. Steps to setup virtual enviroment :

> 1.    First install the virtualenv package into the main machine useing pip:
<br>
For Linux: ``` pip3 install virtualenv```

> 2.    After install virtualenv package creat a virtual enviroment useing this command:
<br>
For Linux: ```python3 -m venv .venv ``` Here .venv is the name of the virtual enviroment, we can give any name for it. 

> 3. We can install package from the requirement.txt file by useing this command:

> 3. Now we need to activate the enviroment with help of this command:
<br>
For Linux: ``` source .venv/bin/activate ``` Here .venv the name of the virtual enviroment.

> 4. Now we can install locally any python package inside the enviroment and use it

> 5. Now we can see what package is install inside the env with help of pip command: ```pip list```

> 6. Useing command: ```pip list > requirement.txt``` We can create a text file where all install package information available as a text.

> 7. Install all package from requirement.txt useing this command: ```python -m pip install -r requirements.txt```

> 8. We need to deactivate the env to exit from it