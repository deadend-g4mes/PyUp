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
Install the PyUp library using the follow command.
```
  pip install PyUp-LifeUp-API
```
You will also need to install requests since the requirements.txt isn't working currently.
```
pip install requests
```
### Setup
Once pip finishes installing the PyUp Library, initialize the PyUp API like so

The `PyUp` class will be used as the basis for all API interactions. 
You can add the other modules by adding `, module-name` after `from pyup import PyUp`.

# General Class
The General class is a class of the pyup library that focuses on the most basic LifeUp API interactions.
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')
up_gen = General(pyup)
```

## General.toast
### a method for sending custom pop-up messages to the LifeUp API
returns request.Response
### ---code example---
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')
up_gen = General(pyup)

popup_result = up_gen.toast(text='example text')
```
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

## General.reward
### a method for sending a custom reward to the LifeUp API
returns request.Response
### ---code example---
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')
up_gen = General(pyup)

reward_result = up_gen.reward(content='example text', type='coin', number=10)
```
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

## General.penalty
### a method for sending a custom Penalty to the LifeUp API
returns request.Response
### ---code example---
```python
from pyup import PyUp, General

pyup = PyUp('host_ip', 'port')
up_gen = General(pyup)
popup_result = up_gen.penality(content='example text', type='coin', number=10)
```
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

# Task Class
The Task class is a class of the pyup library that focuses on task related API calls for the LifeUp API.
```python
from pyup import PyUp, Task

pyup = PyUp('host_ip', 'port')
up_task = Task(pyup)
```

## Task.add_task
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Task

pyup = PyUp('host_ip', 'port')
up_task = Task(pyup)

up_task.add_task()
```
### ---parameters--

## Task.complete_task
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Task

pyup = PyUp('host_ip', 'port')
up_task = Task(pyup)

up_task.complete_task()
```
### ---parameters--

## Task.give_up_task
### description
returns request.Response
### ---code example---
```
```
### ---parameters--

## Task.freeze_task
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Task

pyup = PyUp('host_ip', 'port')
up_task = Task(pyup)

up_task.freeze_task()
```
### ---parameters--

## Task.unfreeze_task
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Task

pyup = PyUp('host_ip', 'port')
up_task = Task(pyup)

up_task.unfreeze_task()
```
### ---parameters--

## Task.delete_task
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Task

pyup = PyUp('host_ip', 'port')
up_task = Task(pyup)

up_task.delete_task()
```
### ---parameters--

# Shop Class
The Shop class is a class of the pyup library that focuses on shop related API calls for the LifeUp API.
```
from pyup import PyUp, Shop

pyup = PyUp('host_ip', 'port')
up_shop = Shop(pyup)
```

## Shop.add_item
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Shop

pyup = PyUp('host_ip', 'port')
up_shop = Shop(pyup)

up_shop.add_item()
```
### ---parameters---

## Shop.edit_item
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Shop

pyup = PyUp('host_ip', 'port')
up_shop = Shop(pyup)

up_shop.edit_item()
```
### ---parameters---

## Shop.use_item
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Shop

pyup = PyUp('host_ip', 'port')
up_shop = Shop(pyup)

up_shop.use_item()
```
### ---parameters---

## Shop.edit_loot_box
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Shop

pyup = PyUp('host_ip', 'port')
up_shop = Shop(pyup)

up_shop.edit_loot_box()
```
### ---parameters---

#  ATM Class
The ATM class is a class of the pyup library that focuses on ATM related API calls for the LifeUp API.
```
from pyup import PyUp, ATM

pyup = PyUp('host_ip', 'port')
up_atm = ATM(pyup)
```

## ATM.deposit
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, ATM

pyup = PyUp('host_ip', 'port')
up_atm = ATM(pyup)

up_atm.deposit()
```
### ---parameters---

## ATM.withdraw
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, ATM

pyup = PyUp('host_ip', 'port')
up_atm = ATM(pyup)

up_atm.withdraw()
```
### ---parameters---


#  Pomodoro Class
The Pomodoro class is a class of the pyup library that focuses on Pomodoro related API calls for the LifeUp API.
```
from pyup import PyUp, Pomodoro

pyup = PyUp('host_ip', 'port')
up_pomo = Pomodoro(pyup)
```

## Pomodoro.add_record
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Pomodoro

pyup = PyUp('host_ip', 'port')
up_pomo = Pomodoro(pyup)

up_pomo.add_record()
```
### ---parameters---

## Pomodoro.edit_pomodoro
### description
returns request.Response
### ---code example---
```
from pyup import PyUp, Pomodoro

pyup = PyUp('host_ip', 'port')
up_pomo = Pomodoro(pyup)

up_pomo.edit_pomodoro()
```
### ---parameters---
