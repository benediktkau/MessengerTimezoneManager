import sys
from dateutil import parser
import pytz
import subprocess
import datetime

def main():

    # Get user input
    timeInput = sys.argv[1]
    timeLocal = parser.parse(timeInput)

    # Create both timezone objects
    old_timezone = "Europe/London"
    new_timezone = "Europe/Berlin"

    # Calculate timezone difference
    timeLocal, timeAbroad = timezoneShift(timeLocal, old_timezone, new_timezone)

    # Transform times into correct string format
    timeLocal, timeAbroad = timeToString(timeLocal, timeAbroad)

    # Concatenate String
    output = timeAbroad + ' ' + '\U0001F1E9\U0001F1EA' + ' GMT+2' + ' | ' + timeLocal + ' ' + '\U0001F1EC\U0001F1E7' + ' GMT+1'
    print("Copied into clipboard! " + output)

    # Copy to clipboard
    subprocess.run("pbcopy", universal_newlines=True, input=str(output))

def timezoneShift(timeLocal, old_timezone, new_timezone):
    old_timezone = pytz.timezone(old_timezone)
    new_timezone = pytz.timezone(new_timezone)
      
    timeLocal = old_timezone.localize(timeLocal)
    timeAbroad = timeLocal.astimezone(new_timezone)
    
    timeLocal = timeLocal.time()
    timeAbroad = timeAbroad.time()

    return timeLocal, timeAbroad

def timeToString(timeLocal, timeAbroad):
    timeLocal = timeLocal.strftime("%H:%M")
    timeAbroad = timeAbroad.strftime("%H:%M")

    return str(timeLocal), str(timeAbroad)

main()


