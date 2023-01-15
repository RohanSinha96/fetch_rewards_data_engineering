import boto3
import json
import hashlib
import psycopg2
from datetime import date

# Connect with AWS SQS Queue to receive message
client = boto3.client('sqs', endpoint_url='http://localhost:4566' ,region_name = 'us-east-1')

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)

today = date.today()

cur = conn.cursor()

cur.execute("DELETE FROM user_logins")

while True:
    response = client.receive_message(QueueUrl='http://localhost:4566/000000000000/login-queue')
    messages = response.get('Messages')
    if messages:
        for message in messages:
            # Receive message
            res = json.loads(message['Body'])
            
            cols = ['user_id', 'app_version', 'device_type', 'ip', 'locale', 'device_id']
            cols.sort()
            keys = list(res.keys())
            keys.sort()
            
            # Ignore records with incorrect records
            if cols == keys:
                # Encode device ID and IP using SHA-256 encoding
                res['device_id'] =  str(hashlib.sha256(res['device_id'].encode()).hexdigest())
                res['ip'] =  str(hashlib.sha256(res['ip'].encode()).hexdigest())
                
                # Replacing NULL values with blank spaces
                if res['user_id'] == None:
                    res['user_id'] = ''
                
                if res['device_type'] == None:
                    res['device_type'] = ''
                    
                if res['ip'] == None:
                    res['ip'] = ''
                 
                if res['device_id'] == None:
                    res['device_id'] = ''
                
                if res['locale'] == None:
                    res['locale'] = ''
                    
                if res['app_version'] == None:
                    res['app_version'] = ''
                    
                
                # Input to the table
                str_inp = "'" + res['user_id'] + "'" + ',' + "'" + res['device_type'] + "'" + ',' + "'" + res['ip'] + "'" + ',' + "'" + res['device_id'] + "'" + ',' + "'" + res['locale'] + "'" + ',' + str(res['app_version'])[0] + ',' + "'" + str(today) + "'"
                command = "INSERT INTO user_logins VALUES (" + str_inp + ")"
                cur.execute(command)
                conn.commit()
                client.delete_message(QueueUrl='http://localhost:4566/000000000000/login-queue', ReceiptHandle=message['ReceiptHandle'])
    else:
        break
