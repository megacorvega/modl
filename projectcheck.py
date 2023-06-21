######################
# PROJECT NAME CHECK #
######################

import requests
import json
import urllib.request

# Read Modrinth project IDs from list
with open("projects.txt", "r") as f:
  projects = [line.rstrip('\n') for line in f]

pd = open('details.txt','w')

print("Writing project details to list...")

# Cycle through projects and print project names
for project in projects:
  link = "https://api.modrinth.com/v2/project/" + project
  page = requests.get(link).json()

  title = page['title']
  id = page['id']
  item = id + ": " + title
  # print(item)
  pd.write(item)
  pd.write('\n')
pd.close()