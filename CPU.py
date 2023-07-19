"""WMI and  one more calls the class to make the protected call , i has searched internet for the libraries to get the accurate result as much as i can, psutil_ was th """


import wmi
import time

# Connect to the WMI API
c = wmi.WMI()

# Set the monitoring interval and threshold
interval = 1  # seconds
threshold = 80  # percent

# Monitor the CPU usage
try:
    while True:
        # Get the current CPU usage
        cpu_usage = c.Win32_Processor()[0].LoadPercentage

        # Check if the CPU usage exceeds the threshold
        if cpu_usage > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
        else:
            print(f"Monitoring CPU usage...")

        # Wait for the next monitoring interval
        time.sleep(interval)
except KeyboardInterrupt:
    print("Monitoring stopped by user")
except Exception as e:
    print(f"An error occurred while monitoring CPU usage: {e}")

