import smtplib

server = None

try:
    server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    server.login('sriharsha.kamalur@snhu.edu', 'Rashmi000@')
    print("Successfully connected to the SMTP server.")
except Exception as e:
    print("Failed to connect to the SMTP server. Error:", e)
finally:
    if server and server.sock is not None:  # Check if the server is still connected
        server.quit()