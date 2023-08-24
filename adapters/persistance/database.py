import boto3
import json
from config.settings import dynamodb_settings, aws_settings


# Initialize the DynamoDB client
dynamodb = boto3.resource(
    "dynamodb",
    region_name=dynamodb_settings.DYNAMODB_REGION,
    aws_access_key_id=aws_settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=aws_settings.AWS_SECRET_ACCESS_KEY
)

class EventTable:
    def __init__(self, item: dict):
        self.dynamodb = dynamodb
        self.table = self.dynamodb.Table("EventTable")
        self.item = item

    def save(self):
        item = json.loads(json.dumps(self.item))
        self.table.put_item(Item=item)
        return item
