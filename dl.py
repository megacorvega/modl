###########################
# MODRINTH MOD DOWNLOADER #
###########################

import requests
import json
import urllib.request

# Read Modrinth project IDs from list
with open("projects.txt", "r") as f:
  projects = [line.rstrip('\n') for line in f]

# Cycle through projects and download .jar files
for project in projects:
  link = "https://api.modrinth.com/v2/project/" + project + "/version"
  page = requests.get(link).json()

  name = page[0]['name']
  current = page[0]['files']
  url = current[0]['url']
  filename = current[0]['filename']
  version = page[0]['game_versions']

  print("Downloading ", name, " for Minecraft version ", version)
  urllib.request.urlretrieve(url, filename)