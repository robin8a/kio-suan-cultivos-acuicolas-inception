# Insert data

```sh
aws dynamodb put-item \
    --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
    --item \
        '{"id": {"S": "aaa-bbb-ccc-ddd-eee"}, "dateTimestamp": {"N": "1675228261111"}, "deviceID": {"S": "e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "featureID": {"S": "N2"}, "value": {"S": "950"}}'

aws dynamodb put-item \
    --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
    --item \
        '{"id": {"S": "1679368653_e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "dateTimestamp": {"N": "1679368653"}, "deviceID": {"S": "e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "featureID": {"S": "N2"}, "value": {"S": "950"}}'

aws dynamodb put-item \
    --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
    --item \
        '{"id": {"S": "1679369062_e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "dateTimestamp": {"N": "1679369062"}, "deviceID": {"S": "e9f71d4f_72f9_49ca_9512_07275c220cbf"}, "featureID": {"S": "N2"}, "value": {"S": "950"}}'


```



# 

- https://www.youtube.com/watch?v=xHDT4CwjUQE