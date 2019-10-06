import csv
import requests

def getData():
  memberInfo = requests.get('http://localhost:3000/api/users/')
  memberObject = memberInfo.json()
  # print(memberObject)
  columns = []
  if memberObject['code'] == 200:
    data = memberObject['result']

    for user in data:
      # print(user)
      columns.append([user['netId'], user['points']])
  else:
    print("failed get request")
    exit(1)
  
  # print("data",columns)
  return columns


columnNames = ['Netid', 'Points']
columns = getData()
first = True

with open('member-points.csv', 'a') as csvfile:
  writer = csv.writer(csvfile)
  if first:
    writer.writerow(columnNames)
    first = False

  for column in columns:
    writer.writerow(column)
  
csvfile.close()


