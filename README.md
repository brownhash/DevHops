# DevHops
### What does DevHops mean?

Dev stands for Developer and Hops stands for Hopping and together DevHops stands for hopping the operations carried out by the developers.


### What it does?

It currently represents a basic model for a classic load balancer.

### Prerequisites

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev nginx git vim
$ sudo pip3 install virtualenv
$ mkdir ~/flaskproject
$ cd ~/flaskproject
$ virtualenv flaskprojectenv
$ source flaskprojectenv/bin/activate
$ pip3 install gunicorn flask
```

### Execution

```bash
$ cd /home/username/
$ sudo vim /etc/nginx/sites-available/default

  #use this configuration
  server {
    listen       80;
    server_name  your_public_dnsname_here;

    location / {
        proxy_pass http://127.0.0.1:5000;
    }
  }
  
$ sudo systemctl restart nginx
$ git clone https://github.com/sharma1612harshit/DevHops
$ python3 DevHops/main.py

-> Open http://ip_addr
-> use "admin" as username and "root" as password
```
