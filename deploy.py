import subprocess
import requests

username = "Florent"
token = "9887f29efdf8a0378c44d3982a851be94dd1cf2c"
id = "34020008"
domain_name = "florent.pythonanywhere.com"

res = subprocess.run(["pytest"], shell=True, capture_output=True, text=True)


def get_commit_message():
    print("Enter your commit message:")
    return input().strip()


def get_request():
    req = requests.get(
        "https://www.pythonanywhere.com/api/v0/user/{username}/cpu/".format(
            username=username
        ),
        headers={"Authorization": "Token {token}".format(token=token)}
    )

    if req.status_code != 200:
        return False
    else:
        return True

def push():
    message = get_commit_message()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push", "origin", "main"])

def pull():
    req = requests.post(
        "https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/".format(
            username=username,
            id=id
        ),
        headers={"Authorization": "Token {token}".format(token=token),
                 "Content-Type": "application/json"},
        json={"input": "cd ~/mysite && git pull\n"}
    )

    if req.status_code != 200:
        return False
    else:
        return True

def reload():
    req = requests.post(
        "https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/".format(
            username = username,
            domain_name = domain_name
        ),
        headers={"Authorization": "Token {token}".format(token=token)}
    )
    
    if req.status_code != 200:
        return False
    else:
        return True

if res.returncode:
    print("TESTING FAILED")
else:
    print("CONNECTION...")

    while get_request():
        print("SUCCESSFUL CONNECTION")

        push()

        print("PULL...")

        while pull():
            print("PULL COMPLETED")
            print("RELOADING...")

            while reload():
                print("RELOADING COMPLETED")
                break
            break
        break
