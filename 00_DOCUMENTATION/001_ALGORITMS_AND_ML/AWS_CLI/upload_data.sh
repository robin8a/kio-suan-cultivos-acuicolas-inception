#!/bin/bash
echo "Total arguments : $#"
echo "Device Id: $1"
echo "Feature Id: $2"
epoch_date=`date +%s`
echo "Epoch: $epoch_date"
separator="_"
id=$epoch_date$separator$1
echo "ID: $id"
value="950"
export pay_load=\
"{"\
"\"id\": {\"S\": \"$id\"}",\ \
"\"dateTimestamp\": {\"N\": \"$epoch_date\"}",\ \
"\"deviceID\": {\"S\": \"$1\"}"\,\ \
"\"featureID\": {\"S\": \"$2\"}"\,\ \
"\"value\": {\"S\": \"$value\"}"\
"}"

echo "pay_load: $pay_load"

aws dynamodb put-item \
    --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
    --item \
        "$pay_load"
         
# aws dynamodb put-item \
#     --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
#     --item \
#         '{"id": {"S": "1679368066_e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "dateTimestamp": {"N": "1679368066"}, "deviceID": {"S": "e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "featureID": {"S": "N2"}, "value": {"S": "950"}}'

# aws dynamodb put-item \
#     --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
#     --item \
#         '{"id": {"S": "1679368066_e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "dateTimestamp": {"N": "1679368066"}, "deviceID": {"S": "e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "featureID": {"S": "N2"}, "value": {"S": "950"}}'
