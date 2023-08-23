import boto3
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute, MapAttribute
from config.settings import dynamodb_settings, aws_settings


# Initialize the DynamoDB client
dynamodb = boto3.resource(
    "dynamodb",
    region_name=dynamodb_settings.DYNAMODB_REGION,
    aws_access_key_id=aws_settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=aws_settings.AWS_SECRET_ACCESS_KEY
)


class EventTable(Model):
    class Meta:
        table_name = "EventTable"
        region = dynamodb_settings.DYNAMODB_REGION

    event_id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute()
    datetime = UnicodeAttribute()
    short_description = UnicodeAttribute()

# Create the DynamoDB table
def create_tables():
    if not EventTable.exists():
        EventTable.create_table(wait=True)

# Drop the DynamoDB table
def drop_tables():
    if EventTable.exists():
        EventTable.delete_table()
