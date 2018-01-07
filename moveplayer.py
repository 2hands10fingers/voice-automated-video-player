from os import listdir, path
from subprocess import call

computer_name = 'antonionogueras'
moveie_directory = 'Documents/Programming/Voicer/Movies'

moviefolder = '/Users/{}/{}'.format(computer_name, moveie_directory)

string = 'The lion king'

for i in listdir(moviefolder):
	title = i.split('.')
	
	if string.lower() == title[0].lower():
   		vlc = '/Applications/VLC.app/Contents/MacOS/VLC'
		call(['open', '-a', vlc, path.join(moviefolder, i)])
