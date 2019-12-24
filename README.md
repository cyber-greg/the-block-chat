# The BlockcHAT

Chat based on blockchain




# Front-end

#### Requirements

* Node.js  >= 10.9
* The `ionic` cli command


#### Launching the development server

```bash
npm install
ionic serve
```

The frontend server should then be available on http://localhost:8100 by default


# Back-end

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

The test remote server is running on http://91.121.30.34:23027/

Launching remote test server : `python manage.py runserver 0.0.0.0:23027`


# API ENDPOINTS

## LOGIN
`http://91.121.30.34:23027/login/`

POST {"email":userEmail,"password":userPassword} => return 500 or 403 if not allowed / return userID: string

## USERS
`http://91.121.30.34:23027/users/`

GET return all users

`http://91.121.30.34:23027/users/?id=userID`

GET return requested user

## MESSAGES
`http://91.121.30.34:23027/messages/?channel=channelID`

GET return list of messages in requested channel

`http://91.121.30.34:23027/messages/`

POST {"channel":channelID,"author":userID,"content":string} => return BAD REQUEST if incomplete / return list of messages in requested channel

## CHANNEL
`http://91.121.30.34:23027/channels/?id=channelID`

GET return channel infos

`http://91.121.30.34:23027/channels/?chatroom=chatroomID`

GET return all channels infos in the requested chatroom

`http://91.121.30.34:23027/channels/?user=userID`

GET return all channels infos where user is allowed or is admin of the channel related chatroom

## CHATROOM
`http://91.121.30.34:23027/chatrooms/`

GET return all chatrooms infos

`http://91.121.30.34:23027/chatrooms/?id=chatroomID`

GET return chatroom infos
