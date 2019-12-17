#
# Run this script every day, to create a daily markdown
# notes file in a specificed directory. Run the script
# using something like cron, osx automator or windows events manager.
#

import os
import datetime
import calendar

# Set this to your notes directory
DAILY_NOTES_DIR = "ENTER PATH HERE"


now = datetime.datetime.now()

if ( os.path.isdir(DAILY_NOTES_DIR) != True ):
  print("error, daily notes directory does not exist. Please create it first")
  print("--> " + DAILY_NOTES_DIR)
  exit()

yearDir = DAILY_NOTES_DIR + "/" + str(now.year)
todaysFileName = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + ".md"
todaysFileFullPath = yearDir + "/" + todaysFileName

print("-> Checking todays notes file :: " + todaysFileFullPath)

if ( os.path.isdir(yearDir) != True):
  print("--> Creating year directory")
  newDir = DAILY_NOTES_DIR + "/" + str(now.year)
  os.mkdir(newDir)


if (os.path.isdir(yearDir)):

  if(os.path.exists(todaysFileFullPath)):
    
    print("--> todays notes file already exists. Finished.")
    exit()

  else:

    print ("--> Creating todays notes file")
    f= open(todaysFileFullPath,"w+")
    notesHeader = "# Daily Notes - " + str(calendar.day_name[now.weekday()]) + " " + str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    print(notesHeader)
    f.write(notesHeader)
    f.close()