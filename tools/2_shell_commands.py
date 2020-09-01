""" 
Using Shell Commands in Python Scrips
Like many scripting languages, Python can work with shell commands, 
running command line statements just like you would if you were typing 
them in the terminal. This is really useful if you have a command line 
program you want to use in a tool, but you want to control how that program 
is interacted with. 
"""

import subprocess

# Represent the command ls -a /var as a dictionary to use in subprocess.Popen
the_command = ["ls", "-a", "/var"]

# Send the stdout and stderr of the process to variables we can use in the script.
stdout, stderr = subprocess.Popen(the_command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# View the output of each variable.
print("stdout: %s" % stdout)
print("stderr: %s" % stderr)