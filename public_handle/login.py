import requests
import json
import os
import yaml

def get_token():
    config = get_config()
    host = config.get("host")

    url = "{}/user-center/oauth/token".format(host)

    payload = "client_id=dmp&client_secret=dmp&grant_type=password&username=dmp&password=dmp"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "312abffa-1610-3fe8-c635-1519ac09af36"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    content = json.loads(response.content)

    return "Bearer {}".format(content["access_token"])



def get_config():

    path = os.getcwd()
    f = open("{}/public_handle/env/env.yaml".format(path) , encoding="utf-8")
    content = yaml.load(f)
    env = content["env"]
    print(env)

    api_f = open(("{}/public_handle/env/config_{}.yaml".format(path, env)), encoding="utf-8")
    api_content = yaml.load(api_f)
    return api_content