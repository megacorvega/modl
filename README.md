# modl
This program allows you auto update mods from Modrinth based on a modlist you define. Everything is run from the `modl` shell script included in this repo.

## INSTRUCTIONS

 1. Clone this repo directly to your mods folder
 2. Project ids can be added / removed using the commands `./modl -a` and `./modl -r`
 3. Run `./modl -u` to download mods, and move them to the top level of the `mods` folder

> :warning: modl will download the most recent version of the mod, and does not filter for desired Minecraft version.

## COMMON ERRORS
When updating mods:

`json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`

There is most likely an invalid project id in `projects.txt`