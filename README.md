# Automatic_Video_Preprocessing
Automatic preprocessing of videos for image processing


##Description
This python script converts hundreds of experimental tsunami videos (~3TB) into
individual frames automatically. 

## The main steps are:
      1. Read the meta-data file of each video and extract the time stamp
      relative to tsunami generation. 
      2. Synchronize all videos to the same starting time stamp corresponding to
      tsunami generation in the wave basin.
      3. Call "ffmpeg" package in Linux environment for video-to-frame
      conversion. The synchronization stamps are used in each conversion.
