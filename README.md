# Real-Time-Serverless-IOT-Design
Real-Time Serverless IoT Design (SmartFarm Monitor)

## Introduction:
The main role of the project is to learn and understand how realtime IOT sensor data is being travelled to AWS cloud to generate the IOT dashboard and take required actions based on the realtime data. This project simulates IOT sensor data(eg., temperature and humidity) from the thing which is being send to IOTCore(PUB/SUB Topic) and from the topic, subscriber consumes the message in realtime and trigger alerts when the value of the temperature crosses the threshold

## Architecture:
![IOT GIF](https://github.com/user-attachments/assets/8df1f38e-98d5-4ef3-a1d4-dcc207f00fcd)


## AWS Resources Used:
1. Internet of thing (Thing) : Thing are Sensors which are present in the soil [farm] captures the data (eg., temperature and humidity) from the soil and sends it to the IOTCore

2. IOTCORE : It is MQTT broker which has Topics where data generated from the sensors are being collected.

3. MQTT: It is known as Message Queuing Telemetry Transport, is a lightweight, publish-subscribe messaging protocol designed for machine-to-machine communication, particularly in resource-constrained environments like the Internet of Things (IoT)  .

4. X509 CERT: Light weight Certificate being imported to the thing which are used to encrypt the data from the thing before it getting transmit.

5. Lambda : It is the serverless compute service which is used to perform computation.

6. Dynamo DB: It is fully managed, serverless, NoSQL database service.

7. SNS : It is fully managed, serverless notification service which is used to send the notification to the subscribers

## Understanding of Realtime IOT Design:

1. Thing can send millions of data to the topic using Light weight protocol called MQTT protocol because devices has less compute & storage, so instaed of using HTTP/HTTPS using MQTT would be feasible options.

2. Data will be transmitted to AWS Cloud- IOTCORE Service called MQTT broker which collects data in topics and further process to different lambda for analtics and perform required actions based on the data.


## PROJECT WORKING IN REALWORLD:

Sensors which are deployed in the farm called as thing capable of capturing the temperature, humidity and other factors data and sends it to the IOTCore(MQTT broker) using the MQTT protocol. The data which are travelling from the thing are encrypted using x509 certificate. The data wcan be send to multiple MQTT topics and from the topics various subscribers such as lambda can read the message and perform computation such as by taking necessary action based on the temperature threshold. The action would be notifying the owners and can trigger other lambda which inturns turn on the switch of farm sprinklers to water the farm.

## Future Scope of this project:
This project can be extended by sending the realtime data from lambda to IOT Analytics/Opensearch for creating the Realtime dashboards with the line/bar graph of temperature and humidity data.

