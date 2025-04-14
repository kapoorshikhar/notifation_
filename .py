
from plyer import notification

# Title and message for the notification
title = "Reminder"
message = "Hey Alex, don't forget to take a break and drink water!"

# Send the notification
notification.notify(
    title=title,
    message=message,
    timeout=10  # Duration in seconds
)
