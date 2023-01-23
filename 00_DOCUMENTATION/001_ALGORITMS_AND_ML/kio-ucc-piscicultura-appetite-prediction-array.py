import json
import io
# from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont
# https://gist.github.com/Adobe-Android/7825cda6949a9fa55cd5707d8f3a5e28

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
    

for label in DATA_JSON_DETECT_LABELS:
    print ("Label: " + label['Name'])
    print ("Confidence: " + str(label['Confidence']))
    print ("Instances:")
    for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        # print ("Parents:")
        # for parent in label['Parents']:
        #     print ("   " + parent['Name'])
        # print ("----------")
        # print ()

def detect_fishes_in_column(detected_labels):
    detected_labels = 1


