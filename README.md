# CSUAyyy

One command to launch a jupyter notebook server on CSUA! 

No more opening multiple terminals, typing in long ssh commands and copying over port numbers. 
This simple command will ssh into CSUA, start a headless jupyter session and connect the session to your local machine.

Its 4x faster than doing it manually!

![demo](https://i.imgur.com/A2YKoOt.gif)

## Installation

```
pip install csuayyy
```

## Tutorial

All commands start with either `csuayyy` or `csua` for short. 

1. Sign up for a [CSUA account](https://www.csua.berkeley.edu/)
2. Run `csuayyy config` when first setting up, and provide the username, password and the path to the id_rsa.pub file you downloaded when signing up
3. Run `csuayyy serve` to start a jupyter session and connect to it locally

## Note

CSUA is Berkeley's student-run high-performance computing cluster, perfect for training machine learning models ~or mining cryptocurrency~. 
However, it should be simple to run on other server setups! 

This project is currentlly only tested on Mac OS 12.1. Other operating systems and configurations are currently untested.

Feel free to drop an issue if you need help setting up for a non-CSUA server, or CSUA is not working for your system.

