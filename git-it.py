import subprocess
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video",help="small video file")
args = parser.parse_args()

subprocess.run(['rm','-rf','frames/'])
subprocess.run(['mkdir','frames'])
subprocess.run(['git','init'],cwd="frames/")
subprocess.run(['ffmpeg','-i',args.video,'frames/frame-%06d.jpg'])
subprocess.run(['git','init'],cwd='frames/')
subprocess.run(['mv',f'frame-{str(1).zfill(6)}.jpg','frame.jpg'],cwd="frames/")
subprocess.run(['git','add',f'frame.jpg'],cwd="frames/")
subprocess.run(['git','commit','-m',f'frame-{1}'],cwd="frames/")
subprocess.run(['git','submodule','add','./frames/'])

for count,frame in enumerate(os.listdir('frames')[1:]):
	if(frame[-3:]=="jpg"):		
		subprocess.run(['mv',f'frame-{str(count+2).zfill(6)}.jpg','frame.jpg'],cwd="frames/")
		subprocess.run(['git','add','frame.jpg'],cwd="frames/")
		subprocess.run(['git','commit','-m',f'frame-{count}'],cwd="frames/")
# subprocess.run(['cd','../'])
# subprocess.run(['rm','-rf','frames/'])