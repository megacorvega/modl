import requests
import json
import urllib.request

###########################
# MODRINTH MOD DOWNLOADER #
###########################

# INSTRUCTIONS
#
# 1.)  Place this python script in your mods folder
# 2.)  Add Modrinth project IDs to the 'projects.txt' file. (One ID per line)
# 3.)  Run python script
#
# NOTE: This will download the most recent version of the mod, and does not filter for desired Minecraft version.

# Read Modrinth project IDs from list
projects = open("projects.txt", "r").read().strip()

# Convert projects text file to comma separated list
projectList = projects.split("\n")

for projects in projectList:
  link = "https://api.modrinth.com/v2/project/" + projects + "/version"
  page = requests.get(link).json()

  name = page[0]['name']
  current = page[0]['files']
  url = current[0]['url']
  filename = current[0]['filename']
  version = page[0]['game_versions']

  print("Downloading ", name, " for Minecraft version ", version)
  urllib.request.urlretrieve(url, filename)

print("Done!")
