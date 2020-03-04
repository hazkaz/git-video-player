import subprocess
import os
import time
import cv2

root_commit = subprocess.run("git rev-list --max-parents=0 HEAD | tail -n 1".split(" "),stdout=subprocess.PIPE,cwd="frames/")
subprocess.run(['git','checkout',root_commit.stdout],cwd="frames")
logs = subprocess.check_output("git log master --oneline --reverse".split(" ")).decode("utf-8").split('\n')
im = cv2.imread('frames/frame.jpg')
cv2.imshow(f'frame',im)
cv2.waitKey(100)
for log in range(len(logs)):
	checkout_command = f"git checkout {logs[log].split(' ')[0]}"
	print(checkout_command)
	os.system(checkout_command)	
	im = cv2.imread('frames/frame.jpg')
	cv2.imshow(f'frame',im)
	cv2.waitKey(20)
	# time.sleep(1)
	