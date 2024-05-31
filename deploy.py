# RELOAD DON'T WORK !!!

import subprocess
import requests
import time

username = 'Florent'
token = '9887f29efdf8a0378c44d3982a851be94dd1cf2c'
id = '34020008'
domain_name = 'florent.pythonanywhere.com'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username = username
    ),
    headers = {'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

result = subprocess.run(["pytest"], shell = True, capture_output = True, text = True)

def push():
    print("Enter your message:")
    message = input().strip()
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push", "origin", "main"])


def pull():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/'.format(
            username=username,
            id=id
        ),
        headers={'Authorization': 'Token {token}'.format(token=token),
                 'Content-Type': 'application/json'},
        json={'input': 'cd ~/mysite && git pull\n'}
    )
    if response.status_code == 200:
        return True
    else:
        return False

def reload():
    response = requests.post(
        'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
            username = username,
            domain_name = domain_name
        ),
        headers = {'Authorization': 'Token {token}'.format(token = token)}
    )

if result.returncode:
    print("ERROR")
else:
    print("OK")
    push()
    if pull():
        reload()



# import subprocess
# import requests
# import time

# username = 'Florent'
# token = '9887f29efdf8a0378c44d3982a851be94dd1cf2c'
# id = '34020008'
# domain_name = 'florent.pythonanywhere.com'

# # Function to check CPU quota
# def check_cpu_quota():
#     response = requests.get(
#         'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
#             username=username
#         ),
#         headers={'Authorization': 'Token {token}'.format(token=token)}
#     )
#     if response.status_code == 200:
#         print('CPU quota info:')
#         print(response.content)
#     else:
#         print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

# # Function to run tests
# def run_tests():
#     result = subprocess.run(["pytest"], shell=True, capture_output=True, text=True)
#     return result.returncode == 0

# # Function to push changes to Git
# def push():
#     print("Enter your message:")
#     message = input().strip()
#     subprocess.run(["git", "add", "."])
#     subprocess.run(["git", "commit", "-m", message])
#     subprocess.run(["git", "push", "origin", "main"])

# # Function to pull changes from Git
# def pull():
#     response = requests.post(
#         'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/send_input/'.format(
#             username=username,
#             id=id
#         ),
#         headers={
#             'Authorization': 'Token {token}'.format(token=token),
#             'Content-Type': 'application/json'
#         },
#         json={'input': 'cd ~/mysite && git pull\n'}
#     )
#     if response.status_code == 200:
#         return True
#     else:
#         print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
#         return False

# # Function to check the status of the console
# def check_console_status():
#     response = requests.get(
#         'https://www.pythonanywhere.com/api/v0/user/{username}/consoles/{id}/'.format(
#             username=username,
#             id=id
#         ),
#         headers={'Authorization': 'Token {token}'.format(token=token)}
#     )
#     if response.status_code == 200:
#         status = response.json().get('status')
#         return status
#     else:
#         print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
#         return None

# # Function to wait for the console to finish the pull operation
# def wait_for_pull_to_finish():
#     while True:
#         status = check_console_status()
#         if status == "finished":
#             print("Pull operation finished.")
#             break
#         elif status == "running":
#             print("Pull operation still running. Checking again in 5 seconds...")
#             time.sleep(5)
#         else:
#             print("Unexpected console status: {}".format(status))
#             break

# # Function to reload the web app
# def reload():
#     response = requests.post(
#         'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
#             username=username,
#             domain_name=domain_name
#         ),
#         headers={'Authorization': 'Token {token}'.format(token=token)}
#     )
#     if response.status_code == 200:
#         print("Web app reloaded successfully.")
#     else:
#         print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

# # Main workflow
# if __name__ == "__main__":
#     check_cpu_quota()
    
#     if run_tests():
#         print("Tests passed.")
#         push()
#         if pull():
#             wait_for_pull_to_finish()
#             reload()
#     else:
#         print("Tests failed.")
