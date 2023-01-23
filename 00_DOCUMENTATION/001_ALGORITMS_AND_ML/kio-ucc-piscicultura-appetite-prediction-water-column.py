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
    print("Labels detected: " + str(detected_labels))

    count_detected_label_in_columns_json = count_fishes_in_column(detected_labels)
    print("Count labels detected on column: " + str(count_detected_label_in_columns_json))

    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(count_detected_label_in_columns_json)
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
    
def count_fishes_in_column(detected_labels):
    count_fishes = 0
    count_fishes_top = 0
    count_fishes_middle = 0
    count_fishes_bottom = 0

    for label in detected_labels:
        if (label['Name'] == 'Fish'):
            count_fishes = len(label['Instances'])
            print ("Label: " + label['Name'])
            print ("Confidence: " + str(label['Confidence']))
            print ("Instances:")
            for instance in label['Instances']:
                print ("  Bounding box")
                print ("    Top: " + str(instance['BoundingBox']['Top']))
                if (float(instance['BoundingBox']['Top']) < 0.33):
                    count_fishes_top += 1
                if (float(instance['BoundingBox']['Top']) > 0.33 and float(instance['BoundingBox']['Top']) < 0.66):
                    count_fishes_middle += 1
                if (float(instance['BoundingBox']['Top']) > 0.66 and float(instance['BoundingBox']['Top']) < 1):
                    count_fishes_bottom += 1
                print ("  Confidence: " + str(instance['Confidence']))
                print()

    print ('count_fishes: ' + str(count_fishes))
    print ('count_fishes_top: ' + str(count_fishes_top))
    print ('count_fishes_middle: ' + str(count_fishes_middle))
    print ('count_fishes_bottom: ' + str(count_fishes_bottom))

    return { "count_fishes":  str(count_fishes), "count_fishes_top": str(count_fishes_top), "count_fishes_middle": str(count_fishes_middle), "count_fishes_bottom": str(count_fishes_bottom)}
