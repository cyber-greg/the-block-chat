# The BlockcHAT

Chat based on blockchain


## Running

### Front-end

#### Requirements

* Node.js  >= 10.9
* The `ionic` cli command


#### Launching the development server

```bash
npm install
ionic serve
```

The frontend server should then be available on http://localhost:8100 by default


### Back-end

#### Requirements

* Python > 3.5
* `python3-venv` module (packaged with the windows installer, installed separately on linux)
* `python3-pip` module (packaged with the windows installer, installed separately on linux)


#### Launching the development server

From the `back/the_blockchat_rest` directory. The first time, we need to
create a virtual environment for python (it is not strictly required, but
highly recommended) :

```bash
python3 -m venv venv # or simply 'python' on windows
```

Then activate and setup the environment:

```bash
source venv/bin/activate # venv/Scripts/activate on windows
pip install -r requirements.txt # If you are unsure you have all dependencies
./manage.py migrate # If you are unsure your database scheme is up to date
./manage.py runserver
```

The backend server should then be available on http://localhost:8000 by default
