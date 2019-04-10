# DevHops
### What does DevHops mean?

Dev stands for Developer and Hops stands for Hopping and together DevHops means to Hop the operations step carried out by the developers.


### What it does?

It currently represents a basic model for a classic load balancer.

### Prerequisites

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev nginx
$ sudo pip3 install virtualenv
$ mkdir ~/flaskproject
$ cd ~/flaskproject
$ virtualenv flaskprojectenv
$ source flaskprojectenv/bin/activate
$ pip install gunicorn flask
$ sudo apt-get install git
```

### Execution

```bash
$ git clone https://github.com/sharma1612harshit/DevHops
$ cd DevHops
$ python3 main.py

-> Open http://localhost:5000/
```
