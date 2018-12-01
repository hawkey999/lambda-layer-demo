import json
import os
import test2
import requests


def lambda_handler(event, context):

    os.system('df')
    os.system('uname -a')
    os.system('ls -l /opt/python')
    print(test2.var_from_test2)

    response = requests.get("http://z.cn")

    return{
        'statusCode': 200,
        'body': json.dumps(response, default=str)
    }
