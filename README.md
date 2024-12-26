# PyUp
### a Python Library for easy usage of the LifeUp API.

## Table of Contents
- [Getting Started](#getting-started)
- [General Class](#general-class)
  - [General.toast](#generaltoast)
  - [General.reward](#generalreward)
  - [General.penalty](#generalpenalty)
## Getting Started
### installing the package
```
  pip install PyUp-LifeUp-API
  pip install requests
```
### Setup
Once pip finishes installing the PyUp Library, initialize the PyUp API like so

The `PyUp` class will be used as the basis for all API interactions. 
You can add the other modules by adding `, module-name` after `from pyup import PyUp`.

# General Class
The General class is a class of the pyup library that focuses on the most basic LifeUp API interactions. This class has three methods in it. `toast`, `reward` and `penalty`
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')
```
## General.toast
### a method for sending custom pop-up messages to the LifeUp API
returns request.Response
### ---parameters---
### text
the message that appears on the prompt.
</br> `str`
### (optional) type
a number from 0-6 defining the text style.
</br> `str`
### (optional) isLong
display duration, True = long, False = short.
</br> `str`
### ---code example---
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')

popup_result = General(pyup).toast(text='example text')
```
## General.reward
### a method for sending a custom reward to the LifeUp API
returns request.Response
### ---parameters---
### content 
text that appears on the reward notification
</br>`str`
### type
reward type (must be either 'coin', 'exp' or 'item').
</br>`str`
### number
amount of reward given.
</br>`int`
### (optional) skills
array of numbers greater than 0. dicates what skills recieve the exp reward.
</br>`list`
### (optional) item_id
the numerical id of the item the user recieves as a reward.
</br>`int`
### (optional) item_name
the name of the item the user recieves as a reward.
</br>`str`
### (optional) silent
wether the UI notification appears or not.
</br>`bool`
### ---code example---
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')

reward_result = General(pyup).reward(content='example text', type='coin', number=10)
```

## General.penalty
### a method for sending a custom Penalty to the LifeUp API
returns request.Response
### ---parameters---
### content 
text that appears on the penalty notification
</br>`str`
### type
penality type (must be either 'coin', 'exp' or 'item').
</br>`str`
### number
amount of penality taken.
</br>`int`
### (optional) skills
array of numbers greater than 0. dicates what skills recieve the exp penality.
</br>`list`
### (optional) item_id
the numerical id of the item the user recieves as a penality.
</br>`int`
### (optional) item_name
the name of the item the user recieves as a penality.
</br>`str`
### (optional) silent
wether the UI notification appears or not.
</br>`bool`
### ---code example---
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')

popup_result = General(pyup).toast(content='example text', type='coin', number=10)
```
