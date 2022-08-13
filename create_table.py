import boto3

dynamodb = boto3.resource("dynamodb")

table = dynamodb.create_table(
    TableName="hosts",
    KeySchema=[
        {"AttributeName": "name", "KeyType": "HASH"},
        {"AttributeName": "ip", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "name", "AttributeType": "S"},
        {"AttributeName": "ip", "AttributeType": "S"},
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
)

table.wait_until_exists()
print(table.item_count)
