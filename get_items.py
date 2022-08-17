import boto3


def get_item():

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("hosts")
    response = table.get_item(Key={"name": "@root", "ip": "192.168.65.6"})
    item = response["Item"]
    print(item)


get_item()
