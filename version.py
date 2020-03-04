import subprocess
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video",help="small video file")
args = parser.parse_args()

subprocess.run(['rm','-rf','frames/'])
subprocess.run(['mkdir','frames'])
subprocess.run(['ffmpeg','-i',args.video,'frames/frame-%06d.jpg'])
subprocess.run(['git','submodule','init'],cwd='frames/')
for count,frame in enumerate(os.listdir('frames')):
	if(frame[-3:]=="jpg"):		
		subprocess.run(['mv',f'frame-{str(count).zfill(6)}.jpg','frame.jpg'],cwd="frames/")
		subprocess.run(['git','add','frame.jpg'],cwd="frames/")
		subprocess.run(['git','commit','-m',f'frame-{count}'],cwd="frames/")
# subprocess.run(['cd','../'])
# subprocess.run(['rm','-rf','frames/'])