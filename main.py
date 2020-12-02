"""
Author: Abhishek Anil Deshmukh
Send unique voter id's to voters via gmail
"""
# token generation
from random import shuffle
from secrets import token_urlsafe

# to get the emails in
from pandas import read_csv

# email stuff
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tqdm import tqdm

VOTER_MAIL_IDS_FILE_LOCATION = "./email_ids.csv"
VOTER_IDS_FILE_LOCATION = "./voter_ids.csv"
COLUMN_NAME = "mail_ids"
LENGTH_OF_VOTER_ID = 16
SUBJECT_OF_MAIL = "Student Gymkhana Election 2020"

# one set of email id and password per ~500 emails
EMAIL_IDS = ["EMAIL ID HERE", "EMAIL ID HERE"]
PASSWORDS = ["CORRESPONDING PASSWORD HERE", "CORRESPONDING PASSWORD HERE"]


def main():
    # importing email ids and shuffling them
    mail_ids = list(read_csv(VOTER_MAIL_IDS_FILE_LOCATION)[COLUMN_NAME])
    shuffle(mail_ids)
    print(f"sending to:{mail_ids}")
    print(f"total of {len(mail_ids)} emails")
    if input("Do you want to continue sending? [Y/N]") != "Y":
        return

    print("Generating voter ids...")
    # generating voter_ids
    voter_ids = []
    for i in range(len(mail_ids)):
        voter_ids.append(token_urlsafe(LENGTH_OF_VOTER_ID))

    # saving the voter_ids
    with open(VOTER_IDS_FILE_LOCATION, "w+") as voter_ids_file:
        voter_ids_file.writelines(map(lambda x: x + "\n", voter_ids))

    print("Logging in")
    ON_EMAIL_ID = 0
    # getting mail server ready
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL_IDS[ON_EMAIL_ID], PASSWORDS[ON_EMAIL_ID])

    print("Starting sending mail")
    for i in tqdm(range(len(voter_ids))):
        # getting mail ready
        body = f"""Dear all,
PLEASE IGNORE THE LAST VOTER-IDS IF YOU GOT ONE, THIS IS YOUR VOTER-ID
Please find the details of Students' Gymkhana Election 2020 below.
Election Procedure: Currently there are 844 students in NISER. Only the existing students will be provided with a unique randomized 'Voter ID'. The election will be conducted through a google form in which it is mandatory for the students to write their 'Voter ID'. If someone shares one's Voter ID it's their own fault; we will consider the first casted vote only corresponding to each 'Voter ID'. Since the 'Voter ID' is random and in no way related to anyone's email-id, the anonymity of each voter is maintained.
Election Timing: 3 pm to 11:59 pm, today.
Voting Form: The link to the google form of election is https://forms.gle/Jsot3scBh2ND27G48.
Your Voter ID: {voter_ids[i]}
For any other query reply to this mail.
Happy Electioneering!!!
Regards,Election Commission"""
        # the email
        msg = MIMEMultipart()
        msg["From"] = EMAIL_IDS[ON_EMAIL_ID]
        msg["Subject"] = SUBJECT_OF_MAIL
        msg["To"] = mail_ids[i]
        msg.attach(MIMEText(body, 'plain'))

        # sending mail with error handeling
        try:
            server.sendmail(EMAIL_IDS[ON_EMAIL_ID], mail_ids[i], msg.as_string())
        except Exception as e:
            # logging in to the new email
            ON_EMAIL_ID += 1
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(EMAIL_IDS[ON_EMAIL_ID], PASSWORDS[ON_EMAIL_ID])
            try:
                server.sendmail(EMAIL_IDS, mail_ids[i], msg.as_string())
            except Exception as e2:
                print(e)
                print(e2)
                print(mail_ids[i])

    print("Done.")


if __name__ == "__main__":
    main()
