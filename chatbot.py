import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("custom.py.aiml")

# Press CTRL-C to break this loop
while True:

    print (kernel.respond(input("enter your message>>")))
    
