import json
import io
# from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont
# https://gist.github.com/Adobe-Android/7825cda6949a9fa55cd5707d8f3a5e28
# https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/doc_source/images-displaying-bounding-boxes.md

DATA_JSON_DETECT_LABELS = [
    {
        "Name": "Aquatic",
        "Confidence": 99.99974822998047,
        "Instances": [],
        "Parents": [
            {
                "Name": "Water"
            }
        ]
    },
    {
        "Name": "Water",
        "Confidence": 99.99974822998047,
        "Instances": [],
        "Parents": []
    },
    {
        "Name": "Aquarium",
        "Confidence": 99.99669647216797,
        "Instances": [],
        "Parents": [
            {
                "Name": "Animal"
            },
            {
                "Name": "Fish"
            },
            {
                "Name": "Sea Life"
            },
            {
                "Name": "Water"
            }
        ]
    },
    {
        "Name": "Fish",
        "Confidence": 99.99669647216797,
        "Instances": [
            {
                "BoundingBox": {
                    "Width": 0.3310309052467346,
                    "Height": 0.25657129287719727,
                    "Left": 0.42200613021850586,
                    "Top": 0.38252711296081543
                },
                "Confidence": 99.64865112304688
            },
            {
                "BoundingBox": {
                    "Width": 0.19113337993621826,
                    "Height": 0.22977054119110107,
                    "Left": 0.42664986848831177,
                    "Top": 0.6660301089286804
                },
                "Confidence": 98.78649139404297
            },
            {
                "BoundingBox": {
                    "Width": 0.19135227799415588,
                    "Height": 0.2786744236946106,
                    "Left": 0.3939155638217926,
                    "Top": 0.08719141781330109
                },
                "Confidence": 89.29351806640625
            },
            {
                "BoundingBox": {
                    "Width": 0.15086981654167175,
                    "Height": 0.16460847854614258,
                    "Left": 0.8102371096611023,
                    "Top": 0.7006813287734985
                },
                "Confidence": 85.830322265625
            }
        ],
        "Parents": [
            {
                "Name": "Animal"
            },
            {
                "Name": "Sea Life"
            }
        ]
    },
    {
        "Name": "Sea Life",
        "Confidence": 99.99669647216797,
        "Instances": [],
        "Parents": [
            {
                "Name": "Animal"
            }
        ]
    },
    {
        "Name": "Animal",
        "Confidence": 99.99669647216797,
        "Instances": [],
        "Parents": []
    }
]

# for label in DATA_JSON_DETECT_LABELS:
# 	print "{Name} - {Confidence}%".format(**label)
    
count_fishes = 0
count_fishes_top = 0
count_fishes_middle = 0
count_fishes_bottom = 0

for label in DATA_JSON_DETECT_LABELS:
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


            # print ("    Left: " + str(instance['BoundingBox']['Left']))
            # print ("    Width: " +  str(instance['BoundingBox']['Width']))
            # print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        # print ("Parents:")
        # for parent in label['Parents']:
        #     print ("   " + parent['Name'])
        # print ("----------")
        # print ()

print ('count_fishes: ' + str(count_fishes))
print ('count_fishes_top: ' + str(count_fishes_top))
print ('count_fishes_middle: ' + str(count_fishes_middle))
print ('count_fishes_bottom: ' + str(count_fishes_bottom))

def count_fishes_in_column(detected_labels):
    count_fishes = 0
    count_fishes_top = 0
    count_fishes_middle = 0
    count_fishes_bottom = 0

    for label in DATA_JSON_DETECT_LABELS:
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

    return { count_fishes:  str(count_fishes), count_fishes_top: str(count_fishes_top)}



