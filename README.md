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


### Back-end

#### Requirements

* Python > 3.5
* `python3-venv` module (packaged with the windows installer, installed separately on linux)
* `python3-pip` module (packaged with the windows installer, installed separately on linux)


#### Launching the development server

From the `back/the_blockchat_rest` directory:

```bash
python3 -m venv venv # or simply 'python' on windows
source venv/bin/activate # venv/Scripts/activate on windows
pip install -r requirements.txt
./manage.py runserver
```
