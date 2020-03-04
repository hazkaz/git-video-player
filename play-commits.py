import subprocess
import os
import time
import cv2


parent_commits = subprocess.Popen("git rev-list --max-parents=0 HEAD".split(" "),stdout=subprocess.PIPE,cwd="frames/")
root_commit = subprocess.run(['tail','-n','1'],stdin=parent_commits.stdout,stdout=subprocess.PIPE)
parent_commits.wait()
subprocess.run(['git','checkout',root_commit.stdout],cwd="frames/")
logs = subprocess.check_output("git log master --oneline --reverse".split(" "),cwd="frames/").decode("utf-8").split('\n')
im = cv2.imread('frames/frame.jpg')
cv2.imshow(f'frame',im)
cv2.waitKey(100)
for log in range(len(logs)):
	checkout_command = f"git checkout {logs[log].split(' ')[0]}"
	print(checkout_command)
	subprocess.run(checkout_command.split(" "),cwd="frames/")	
	im = cv2.imread('frames/frame.jpg')
	cv2.imshow(f'frame',im)
	cv2.waitKey(20)
	# time.sleep(1)
	