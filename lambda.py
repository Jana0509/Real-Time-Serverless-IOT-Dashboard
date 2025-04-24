import json
import boto3
import os
from datetime import datetime
from decimal import Decimal  # <-- This is key

# Initialize clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Environment variables
DYNAMODB_TABLE = os.environ.get('DYNAMODB_TABLE', 'SmartFarmReadings')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', 'arn:aws:sns:us-east-1:484907514055:SmartFarmAlerts')
TEMP_THRESHOLD = float(os.environ.get('TEMP_THRESHOLD', 35.0))

table = dynamodb.Table(DYNAMODB_TABLE)

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))

        payload = event
        if 'deviceId' not in payload:
            # Sometimes the payload is nested in 'message' or 'payload'
            payload = json.loads(event.get('payload', '{}'))

        device_id = payload.get('deviceId', 'unknown')
        temperature = Decimal(str(payload.get('temperature', 0)))
        humidity = Decimal(str(payload.get('humidity', 0)))
        timestamp = payload.get('timestamp') or datetime.utcnow().isoformat()

        # Save to DynamoDB
        table.put_item(Item={
            'deviceId': device_id,
            'timestamp': timestamp,
            'temperature': temperature,
            'humidity': humidity
        })

        print(f"Data saved to DynamoDB for {device_id}")

        # Trigger alert
        if float(temperature) > TEMP_THRESHOLD:
            alert_message = f"🔥 High temperature alert!\nDevice: {device_id}\nTemp: {temperature}°C\nTime: {timestamp}"
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject="SmartFarm Temperature Alert",
                Message=alert_message
            )
            print("Alert sent to SNS")

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Sensor data processed successfully'})
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

