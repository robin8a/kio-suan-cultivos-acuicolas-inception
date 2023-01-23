import json
import boto3
import io
import time

def lambda_handler(event, context):
    json_body = json.loads(event.get('body'))
    # json_body = event
    project_arn='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/1666802909250'
    model_arn='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/version/fish-illness-detection.2022-10-26T14.57.51/1666814271805'
    min_inference_units=1 
    version_name='fish-illness-detection.2022-10-26T14.57.51'
    
    # Testing de Model
    bucket='kiosuancultacuicv2bb5d71c6f2fe40ffaad66a34b8c47115340-dev'
    key='public/appetite_prediction/'+json_body['photo']
    model='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/version/fish-illness-detection.2022-10-26T14.57.51/1666814271805'
    min_confidence=80

    detected_labels = detect_labels(bucket, key, min_confidence)
    print("Custom labels detected: " + str(detected_labels))
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(detected_labels)
    }


def detect_labels(bucket, key, min_confidence):
    client=boto3.client('rekognition')

    #Call DetectCustomLabels
    response = client.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=10,
		MinConfidence=min_confidence,
	)
    
    print(response)
    # For object detection use case, uncomment below code to display image.
    # display_image(bucket,photo,response)

    return response['Labels']
    
def detect_fishes_in_column(detected_labels):
    detected_labels = 1
