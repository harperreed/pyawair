from awair import awair

if __name__ == "__main__":
    import datetime

    username = "email@gmail.com" #The email you use to login to Awair
    password = "very long and secure password" #The secure password you use to login to awair

    api =  awair(username, password) #Let's authenticate

    devices = api.devices() #Grab the devices that are on your account
    
    today = datetime.datetime.today() 
    yesterday = today - datetime.timedelta(days=1)

    for device in devices:  #Let's iterate through devices
      print(device) #Print the device 

      print("Let's grab the weather")
      print(api.weather(latitude=device['latitude'],longitude=device['longitude']))

      print("Timeline from yesterday to today")
      print(api.timeline(device['id'], str(yesterday.isoformat()), str(today.isoformat())))
      
      print("Event score")
      print api.events_score(device['id'])
      
      device_id = device['id'] #Store the last device id for the next part


    inbox = api.inbox() #Grab inbox
    for message in inbox: #iterate through messages in inbox
      print message #Print the message
      
      if message['title']=='Sleep Report':
        print("Printing sleep report for " + message['timestamp'])
        print(api.sleep_report(device_id, message['timestamp']))
