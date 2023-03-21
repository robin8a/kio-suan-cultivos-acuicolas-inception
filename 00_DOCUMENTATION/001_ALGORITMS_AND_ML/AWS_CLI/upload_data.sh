#!/bin/bash
# .properties file
. /home/pi/Adafruit_Python_DHT/examples/conf.properties

# ./upload_data.sh e9f71d4f_72f9_49ca_9512_07275c220cbf temperatura_agua humedad
# Variable load to global use in other scripts
export REC_LOG_FILE=$conf_logs_path"rec_"$(date +%d-%m-%Y)".log"
export rec_today_date=$(date +"%d-%m-%Y")

epoch_date=`date +%s`
separator="_"
id_temp=$epoch_date$separator$1$separator$2
id_huminity=$epoch_date$separator$1$separator$3


# Temp and Huminity 
cd $conf_python_path
temp_and_huminity=`sudo ./AdafruitDHT.py 22 21`
IFS='= ' read -r -a array <<< "$temp_and_huminity"
temp=${array[1]}
huminity=${array[3]}

export pay_load_temp=\
"{"\
"\"id\": {\"S\": \"$id_temp\"}",\ \
"\"dateTimestamp\": {\"N\": \"$epoch_date\"}",\ \
"\"deviceID\": {\"S\": \"$1\"}"\,\ \
"\"featureID\": {\"S\": \"$2\"}"\,\ \
"\"value\": {\"S\": \"$temp\"}"\
"}"

export pay_load_huminity=\
"{"\
"\"id\": {\"S\": \"$id_huminity\"}",\ \
"\"dateTimestamp\": {\"N\": \"$epoch_date\"}",\ \
"\"deviceID\": {\"S\": \"$1\"}"\,\ \
"\"featureID\": {\"S\": \"$3\"}"\,\ \
"\"value\": {\"S\": \"$huminity\"}"\
"}"

# Logs
echo "$(date +"%m-%d-%Y %H:%M:%S"): Today date: $rec_today_date" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Total arguments: $#" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Device Id: $1" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Feature Id: $2" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Epoch: $epoch_date" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): id: $id" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Temp and Huminity: $temp_and_huminity" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Temp: $temp" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): Huminity: $huminity" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): #######: $pay_load" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): pay_load_temp: $pay_load" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): #######: $pay_load_temp" >> $REC_LOG_FILE
echo "$(date +"%m-%d-%Y %H:%M:%S"): pay_load_huminity: $pay_load_huminity" >> $REC_LOG_FILE

aws dynamodb put-item \
    --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
    --item \
        "$pay_load_temp"


aws dynamodb put-item \
    --table-name DeviceFeature-yqpez3p3ufgjlaxina465nwpri-dev  \
    --item \
        "$pay_load_huminity"
