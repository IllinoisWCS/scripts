import pandas as pd
import requests

import sys

print(len(sys.argv))
if len(sys.argv) != 4:
  print("check input args")
  exit(1)

csvName = sys.argv[1]
eventId = sys.argv[2]
eventKey = sys.argv[3]


df = pd.read_csv(csvName)
saved_column = df.NetID
for userid in saved_column[1:]:
  eventRequest = requests.put("http://localhost:3000/api/events/"+eventId, data={'event_id':eventId, 'netid':userid, 'event_key':eventKey})
  if eventRequest.status_code == 200:
    print("added to even successfully")
    print(eventRequest.reason)
    print(eventRequest.text[:300] + '...')

    userRequest = requests.put("http://localhost:3000/api/users/" + userid, data={'key':eventKey} )
    if userRequest.status_code == 200:
      print('successfully added points to ' + userid)
    else:
      print('failed to add points for ' + userid)
  else:
    print(eventRequest.reason)
    print(eventRequest.text[:300] + '...')
    print("failed to add " + userid + " to event")
    exit(1)
  # print("data",data, len(data))
  # exit(0)

# print(saved_column)