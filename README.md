# Git powered video player

#### Imagine...if all you had to do to watch a movie was clone a repo.

<span style="font-size:10px">Well that hasn't happened yet, but this is a first step in that direction</span>

Starting with the first frame of the movie, each new frame is a commit in the repository.

This is the end result of _git checkout_-ing very fast through all the frames

👀

![](demo.gif)

```python
# commit frame by frame
python3 git-it.py

# checkout and play fram by fram
python3 play-commits.py
```


#### pre-requisites
1. ffmpeg
2. git