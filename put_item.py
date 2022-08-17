import boto3


def put_item():

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("hosts")
    table.put_item(
        Item={"name": "@eliot", "ip": "191.168.65.6"},
    )
    table.put_item(
        Item={"name": "lucasjt", "ip": "191.168.65.5"},
    )

    print("Done")


put_item()
