import os
import re

from datetime import datetime
from pathlib import Path

'''
	movieFolders = os.listdir()
	for title in movieFolders:
		print(title.replace(' ', '.'))
	
	spider-man.into.the.spider-verse.2018.720p.bluray.x264-nezu.mkv
	The.Suicide.Squad.2021.720p.HMAX.WEBRip.900MB.x264-GalaxyRG.mkv
	The.Chronicles.of.Narnia.The.Lion.The.Witch.And.The.Wardrobe.2005.720p.Brrip.x264.Deceit.YIFY.mp4)

--- Pseudo Code ---
1 Check the ~/Videos/ Folder to see if there are any other files/folders than 'temp'
	If File
			If file has 'e02', 'E10', etc. 
					then it is part of a show
			If not and does not have 'S01' etc, it is a movie file.
					- must be put into a folder of it's own movie for organization
	If Folder
			If folder has 'S01', 's02', etc. 
					then it is a show folder
						Strip off everything after the season number (eg. 'S01')
							Enter folder
								for each file
									strip everything after the 'S01E01' of the video files
										Move folder into shows path
			If folder does not have 'S02' or anything
					then it is a movie folder
						strip off everything after the 4 digit date.
							Enter folder
								For each File
									Strip everything after the 4 digit date of the video file
										move folder into movies path
'''

# Folder to check for new Folders or Files
VIDEOS_PATH = "/home/epoch/Videos/"

# Paths to the movie/show folders
MOVIES_PATH = "/run/media/epoch/Video/Videos/Movies/"
SHOWS_PATH = "/run/media/epoch/Video/Videos/Shows/"

videosFolder = Path(VIDEOS_PATH)
moviesFolder = Path(MOVIES_PATH)
showsFolder = Path(SHOWS_PATH)

# Add FOLDERS/FILES that you want to be overlooked
FOLDERS_FILES_TO_SKIP = ['temp', 'Torrent-Sorter']

def printMovieDestinationFolder():
	print("------- Movie Folders -------")
	for item in moviesFolder.iterdir():
		if item.is_file():
			print(item.name)
		else:
			for file in item.iterdir():
				print(file.name)

def printShowDestinationFolder():
	print("------- Show Folders -------")
	for show in showsFolder.iterdir():
		print(show.name)

def checkForNewDownloads():
	new_downloads = []
	for item in videosFolder.iterdir():
		if item.name in FOLDERS_FILES_TO_SKIP:
			pass
		else:
			new_downloads.append(item)
	if len(new_downloads) == 0:
		return(None)
	else:
		return(new_downloads) # Should be changed to return the list of the newly downloaded files or folders found 

# def 

def renameFolder(folder):
	pass

def renameFile(file):
	print(file.name)
	print(re.search(r'[0-9]+(.*?){}'.format(file.suffix), file.name))
	print()

def renameShowFile(file):
	print(re.search(r'S[0-9]E[0-9]+(.*?){}'.format(file_suffix), file.name))
	print()	

def main():
	# Check Videos Origin Folder
	newDownloads = checkForNewDownloads()
	
	# If there are no new downloads in the folder to check
	# Then exit() and try again later.
	if not newDownloads:
		print("No new torrents at this time...\nRescheduling...")
		exit()
	# Else if there are new files other than the files/folders to overlook
	# Then continue with the rest of the process
	else:
		print("New Downloads Found:")
		for item in newDownloads:
			print(item.name)
			for file in item.iterdir():
				print("\t|-" + file.name)
				# print(dir(file))
				# print(os.path.splitext(file.name))

if __name__ == "__main__":
	main()