import boto3

dynamodb = boto3.resource("dynamodb")


table = dynamodb.Table("hosts")

response = table.delete_item(Key={"name": "@root", "ip": "192.168.65.6"})

print("Done!")
