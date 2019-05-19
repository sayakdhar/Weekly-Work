import os
import subprocess as sp
import pyttsx3
import cv2

os.system("tput setaf 1")
print("\t\t\tWelcome to my tool")

print("\t\t\t---------------")
os.system("tput setaf 0")

print("Where do you want to run your tool(local/remote) : ",end='')
location=input()
if location == "remote":
	print("Enter remote ip : ",end='')
	remote_ip=input()

print("""
Press 1: to check date
Press 2: for cal
Press 3: to take photo
Press 4: to create file
Press 5: exit
""")

speaker = pyttsx3.init()

speaker.say("Enter your choice : ")
speaker.runAndWait()
print("Enter your choice:",end='')
ch=input()
print(ch)

if location =="local":
	if int(ch) == 1:
		x=sp.getoutput("date")
		speaker.say("The date is")
		speaker.runAndWait()
		print(x)
	elif int(ch) == 2:
		y=sp.getoutput("cal")
		print(y)
	elif int(ch) == 3:
		print("Photo Captured")
		sp.getoutput("python36 /root/Desktop/Python\ code/photo.py")
	elif int(ch) == 4:
		print("Enter your file name : ", end='')
		file_name=input()
		sp.getoutput("touch {}".format(file_name))
	elif int(ch) == 5:
		print("exit")
		print("option not supported")
elif location == "remote":
	if int(ch)==1:
		y=sp.getoutput("ssh {} date".format(remote_ip))
		print(y)
	elif int(ch)==2:
		z=sp.getoutput("cal")
		print(z)
	elif int(ch)==3:
		print
else:
	print("Illogical")
