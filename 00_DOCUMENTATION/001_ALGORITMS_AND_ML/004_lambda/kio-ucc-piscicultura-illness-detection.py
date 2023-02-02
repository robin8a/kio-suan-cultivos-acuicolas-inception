import json
import boto3
import io
import time
# from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont

def lambda_handler(event, context):
    json_body = json.loads(event.get('body'))
    # json_body = event
    project_arn='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/1666802909250'
    model_arn='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/version/fish-illness-detection.2022-10-26T14.57.51/1666814271805'
    min_inference_units=1 
    version_name='fish-illness-detection.2022-10-26T14.57.51'
    
    # Staring Model
    start_model(project_arn, model_arn, version_name, min_inference_units)
    
    # Testing de Model
    bucket='kiosuancultacuicv2bb5d71c6f2fe40ffaad66a34b8c47115340-dev'
    photo='public/illness_detection/'+json_body['photo']
    model='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/version/fish-illness-detection.2022-10-26T14.57.51/1666814271805'
    min_confidence=40

    custom_labels = show_custom_labels(model,bucket,photo, min_confidence)
    print("Custom labels detected: " + str(custom_labels))
    
    # Closing model
    model_arn='arn:aws:rekognition:us-east-1:036134507423:project/fish-illness-detection/version/fish-illness-detection.2022-10-26T14.57.51/1666814271805'
    # stop_model(model_arn)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(custom_labels)
    }


#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)


def start_model(project_arn, model_arn, version_name, min_inference_units):

    client=boto3.client('rekognition')

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response=client.start_project_version(ProjectVersionArn=model_arn, MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter('project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn, VersionNames=[version_name])

        #Get the running status
        describe_response=client.describe_project_versions(ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage']) 
    except Exception as e:
        print(e)
        
    print('Done...')

# def display_image(bucket,photo,response):
#     # Load image from S3 bucket
#     s3_connection = boto3.resource('s3')

#     s3_object = s3_connection.Object(bucket,photo)
#     s3_response = s3_object.get()

#     stream = io.BytesIO(s3_response['Body'].read())
#     image=Image.open(stream)

#     # Ready image to draw bounding boxes on it.
#     imgWidth, imgHeight = image.size
#     draw = ImageDraw.Draw(image)

#     # calculate and display bounding boxes for each detected custom label
#     print('Detected custom labels for ' + photo)
#     for customLabel in response['CustomLabels']:
#         print('Label ' + str(customLabel['Name']))
#         print('Confidence ' + str(customLabel['Confidence']))
#         if 'Geometry' in customLabel:
#             box = customLabel['Geometry']['BoundingBox']
#             left = imgWidth * box['Left']
#             top = imgHeight * box['Top']
#             width = imgWidth * box['Width']
#             height = imgHeight * box['Height']

#             fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
#             draw.text((left,top), customLabel['Name'], fill='#00d400', font=fnt)

#             print('Left: ' + '{0:.0f}'.format(left))
#             print('Top: ' + '{0:.0f}'.format(top))
#             print('Label Width: ' + "{0:.0f}".format(width))
#             print('Label Height: ' + "{0:.0f}".format(height))

#             points = (
#                 (left,top),
#                 (left + width, top),
#                 (left + width, top + height),
#                 (left , top + height),
#                 (left, top))
#             draw.line(points, fill='#00d400', width=5)

#     image.show()

def show_custom_labels(model,bucket,photo, min_confidence):
    client=boto3.client('rekognition')

    #Call DetectCustomLabels
    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MinConfidence=min_confidence,
        ProjectVersionArn=model)
    
    print(response)
    # For object detection use case, uncomment below code to display image.
    # display_image(bucket,photo,response)

    return response['CustomLabels']


def stop_model(model_arn):

    client=boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    #Stop the model
    try:
        response=client.stop_project_version(ProjectVersionArn=model_arn)
        status=response['Status']
        print ('Status: ' + status)
    except Exception as e:  
        print(e)  

    print('Done...')