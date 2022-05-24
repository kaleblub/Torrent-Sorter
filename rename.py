import os

from datetime import datetime
from pathlib import Path

''' --- GOALS ---
  ~ Change all spaces to periods.
	IE: (movieFolers = os.listdir()
	   for title in movieFolders:
		print(title.replace(' ', '.'))
	    )

  ~ Save the file type for after all string manipulations
  ~ Remove all text after the Movie Title, Release Date, and Resolution
	IE: (spider-man.into.the.spider-verse.2018.720p.bluray.x264-nezu.mkv
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

# movieFilesList = []
# showsFilesList = []

# ''' Recursive Function To Find All Files In File Structure '''
# def getAllFiles(item, fileList):
# 	# If the item is a file, add it to the list of movies
# 	if item.is_file():
# 		fileList.append(item)
# 	elif item.is_dir():
# 		getAllFiles(item, )


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

def 

def renameFolder(folder):
	pass

def renameFile(file):
	pass

def main():
	# Check Videos Origin Folder
	newDownloads = checkForNewDownloads()
	if not newDownloads:
		print("No new torrents at this time...\nRescheduling...")
		exit()
	else:
		print("New Downloads Found:")
		for item in newDownloads:
			print(item.name)

if __name__ == "__main__":
	main()