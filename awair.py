import requests
import json

class awair:

  def __init__(self, username, password, access_token=None):
    self.username = username
    self.password = password

    if not access_token: 
      self.login()
    else:
      self.access_token = access_token
    self.password = None


  def make_request(self, url, params=None, method='GET'):
    headers = { "Authorization":"Bearer " + self.access_token}
    if params:
      params = urllib.urlencode(params, True).replace('+', '%20')
    if method == 'GET':
      r = requests.get(url, params=params, headers=headers)
    elif method == 'POST':
      r = requests.post(url, params=params, headers=headers)

    response = r.json()

    return response

  def login(self):
    print("logging in")
    url = "https://mobile-app.awair.is/v1/users/login"
    data = {"email":self.username,"password":self.password}
    #headers = {"Authorization":"Bearer MYREALLYLONGTOKENIGOT"}
    response = requests.post(url,json=data).json()
    self.access_token = response['accessToken']
    self.user_id = response['userId']

  def devices(self):
    url = "https://internal.awair.is/v1.1/users/self/devices"
    devices = self.make_request(url, method="GET")['data']
    return devices

  def inbox(self, lang="en",limit="20"):
    url = "https://internal.awair.is/v1/users/self/inbox-items?lang=" + lang + "&limit=" + limit
    inbox = self.make_request(url, method="GET")['data']
    return inbox

  def weather(self, latitude, longitude):
    url = "https://internal.awair.is/v1.2/weather?latitude=" + str(latitude) + "&longitude=" + str(longitude)
    weather = self.make_request(url, method="GET")
    return weather

  def contents(self, latitude, longitude):
    url = "https://contents.awair.is/v1/contents?co2_index=0&dust_index=0&humid_index=2&humid_meta=low&lang=en&load_more=0&preference=General&score=87&score_color=green&temp_index=0&temp_meta=high&voc_index=0"
    contents = self.make_request(url, method="GET")
    return contents

  def events_score(self, device_id, desc="true", limit="1"):
    url = "https://internal.awair.is/v1/devices/awair/"+str(device_id)+"/events/score?desc="+desc+"&limit="+ limit
    events = self.make_request(url, method="GET")
    return events

  def timeline(self, device_id, from_timestamp, to_timestamp):
    url = "https://internal.awair.is/v1.2/devices/awair/"+str(device_id)+"/timeline?from="+from_timestamp+"&to="+to_timestamp
    timeline = self.make_request(url, method="GET")
    return timeline

  def sleep_report(self, device_id, timestamp, lang="en" ):
    url = "https://internal.awair.is/v1.2/users/self/devices/awair/"+str(device_id)+"/sleep-report?lang="+lang+"&timestamp="+timestamp
    timeline = self.make_request(url, method="GET")
    return timeline

