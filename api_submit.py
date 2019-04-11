
# coding: utf-8

import requests

files={'files': open('sample_submission.csv','rb')}

data = {
    "user_id": "zhang_jia9",   #user_id is your username which can be found on the top-right corner on our website when you logged in.
    "team_token": "377e40690f42501bac1b394972bd3c923dc6decd84157c39edf7f371fcaa83d5", #your team_token.
    "description": 'First try submission',  #no more than 40 chars.
    "filename": "sample_submission.csv", #your filename
}

url = 'https://biendata.com/competition/kdd_2018_submit/'

response = requests.post(url, files=files, data=data)

print(response.text)


