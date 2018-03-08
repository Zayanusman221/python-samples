import logging
import json
import greengrasssdk

def function_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    client = greengrasssdk.client("iot-data")

    data = event

    toggle = None
    if("toggle" in data):
        toggle = data["toggle"]

    if(toggle == None):
        logger.info("toggle was never passed to Lambda, exiting.")
        return

    if(toggle.lower() == "on"):
        logger.info("Sending \"On\" signal to coffee machine.")
        topic = "$aws/things/Home_IoT_Devices_Coffee/shadow/update"
        payload = '{"state":{"desired":{"property": "on"}}}'
        client.publish(topic=topic, payload=payload)
    elif(toggle.lower() == "off"):
        logger.info("Sending \"Off\" signal to coffee machine.")
        topic = "$aws/things/Home_IoT_Devices_Coffee/shadow/update"
        payload = '{"state":{"desired":{"property": "off"}}}'
        client.publish(topic=topic, payload=payload)
    else:
        logger.info("Invalid toggle, options are \"on\" or \"off.\"")
