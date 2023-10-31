from datetime import datetime

def timeConversion(s):
    # Parse the input time string in the 12-hour format
    time_12hr = datetime.strptime(s, '%I:%M:%S%p')
    
    # Format the time in the 24-hour format
    time_24hr = time_12hr.strftime('%H:%M:%S')
    
    return time_24hr

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)