# VIDG
Voter ID Generator, made for NISER elections.

## Quick Start

### Voter Email Ids

Write the list of email id's of voters in a file with
- one email id per line and
- file name as `email_ids.csv`
- first line as `mail_ids`

### Login

Open `main.py` and put in the email address and password of the email from which
the emails are to be sent in `line 22` and `23`.

If you are sending the email to over 500 people, Google will log out and you will
have to use a new email, to avoid stopping the emails from sending and figuring
out who the email were sent to and who not too, I would recommend putting in
multiple logins credentials in that list.

### The actual email

- the subject of the email: `SUBJECT_OF_MAIL`
- email body: `line 54`

### Requirements

````
$ pip install -r requirements.txt
````

### Send it

````
$ python3 main.py
````

Each email should take about a couple of seconds

### Voter Ids

Once all the emails are sent, the code will save a list of all the voter ids
sent to voters in a file called `voter_ids.csv`

## Fair Warning

Please recheck things before starting, if you start the code and it stops half
way you will be in trouble as you won't be able to tell who the emails have been
sent to and who not to.
