import subprocess
import requests

username = 'Florent'
token = '9887f29efdf8a0378c44d3982a851be94dd1cf2c'
id= '34020008'
domain_name= 'florent.pythonanywhere.com'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

result = subprocess.run(["pytest"], shell=True, capture_output=True, text=True)

def pull():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/'.format(
            username=username,
            id=id
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

def reload():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
            username=username,
            domain_name=domain_name
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))


def push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "CI/CD"])
    subprocess.run(["git", "push", "origin", "main"])

if result.returncode:
    print("ERROR")
else:
    print("OK")
    push()
    pull()
    reload()