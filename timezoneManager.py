import sys
from dateutil import parser
import pytz
import subprocess
import datetime
import flag

def main():
    # Default local timezone
    defaultTimezone = 'GB'
    timezoneLocal = pytz.country_timezones[defaultTimezone][0]


    # Check if user provided input
    if len(sys.argv) < 2:
        print("Please provide a time in any format.")
        return 1

    # Read user input time
    timeInput = sys.argv[1]

    # Read user input additional timezone
    if len(sys.argv) == 3:
        timezoneInput = sys.argv[2]
        try:
            timezoneAbroad = pytz.country_timezones[timezoneInput][0]
        except KeyError:
            timezoneAbroad = "Europe/" + timezoneInput
    else:
        timezoneAbroad = "Europe/Berlin"

    # Parsing into datetime format
    try:
        timeLocal = parser.parse(timeInput)
    except ValueError:
        print('Sorry, the time format you provided could not be recognized. Please try again!')
        return 1

    # Calculate timezone difference
    timeLocal, timeAbroad = timezoneShift(timeLocal, timezoneLocal, timezoneAbroad)

    # Transform times into correct string format
    timeLocal, timeAbroad = timeToString(timeLocal, timeAbroad)

    # Get flag emoji
    flagAbroad = flag.flag(timezoneInput)
    flagLocal = flag.flag(defaultTimezone)

    # Concatenate String U0001F1E9\U0001F1EA'
    output = flagAbroad + ' ' +  timeAbroad + ' GMT+2' + ' | ' + flagLocal + ' ' +  timeLocal + ' GMT+1'
    print("Copied into clipboard! " + output)

    # Copy to clipboard
    subprocess.run("pbcopy", universal_newlines=True, input=str(output))

def timezoneShift(timeLocal, old_timezone, new_timezone):
    # Define timezones
    old_timezone = pytz.timezone(old_timezone)
    new_timezone = pytz.timezone(new_timezone)
    
    # Assign timezones
    timeLocal = old_timezone.localize(timeLocal)
    timeAbroad = timeLocal.astimezone(new_timezone)
    
    # Delete date from date-timestamp
    timeLocal = timeLocal.time()
    timeAbroad = timeAbroad.time()

    return timeLocal, timeAbroad

def timeToString(timeLocal, timeAbroad):
    # Return hours & minutes only
    timeLocal = timeLocal.strftime("%H:%M")
    timeAbroad = timeAbroad.strftime("%H:%M")

    return str(timeLocal), str(timeAbroad)

main()


