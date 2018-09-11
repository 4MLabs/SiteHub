# SiteHub

Have you ever found interesting sites but storing them in browser markers is messy?
This project is intended to fix it.

Just run it and store your favorite sites ordered by categories.


### Setup

Create virtualenv
```sh
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
```
Run SiteHub
```sh
$ source env/bin/activate

# if is the first time, run -s
# it will create your user, create the db and more
$ python sitehub.py -s

# if not the first time, just do
$ python sitehub.py -r

# for help
$ python sitehub.py -h
```

***Contact: Luis Esteban Rodríguez <rodriguezjluis0@gmail.com>***