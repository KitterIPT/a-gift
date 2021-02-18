# This is my small fun gift for my friend, hope this one bring you joy :)
# Haha, anyway. Happy birthday, Phuong :)
import os
import shutil

"""
import sys
import time

type = {
	# Files extenstion types
	programs : {	'.application': 'Programs',
					'.exe': 'Programs',
					'.air': 'Programs',
					'.msi': 'Programs',
					'.rpm': 'Programs',
					'.dmg': 'Programs',

					'.swf': 'Programs',
					'.apk': 'Programs',
					'.iso': 'Programs',
	},
	documents : {	'.pptx': 'Powerpoints',
					'.ppt': 'Powerpoints',
					'.doc': 'Words',
					'.docx': 'Words',
					'.dotx': 'Words',
					'.xls': 'Excels',
					'.xlsx': 'Excels',		
					'.pdf': 'PDFs',

					'.xml': 'Web',
					'.htm': 'Web',
					'.html': 'Web',
					
					'.odp': 'Documents',
					'.wbk': 'Documents',
					'.odt': 'Documents',

					'.txt': 'Text',
					'.mht': 'Text',

					'.epub': 'Books',
					'.fb2': 'Books',
					'.mobi': 'Books',
					'.djvu': 'Books',

					'.odb': 'Databases',
					'.mwb': 'Databases',
					'.sql': 'Databases',
					'.sql.gz': 'Databases',
					'.tgz': 'Databases',
					'.tar.gz': 'Databases',
					'.csv': 'Databases',

					'.jnlp': 'Scripts',
					'.c': 'Scripts',
					'.sh': 'Scripts',
					'.py': 'Scripts',
					'.phtml': 'Scripts',
					'.php': 'Scripts',
					'.aspx': 'Scripts',
					'.pl': 'Scripts',
					'.js': 'Scripts',

					'.bak': 'Backup',
					'.bk': 'Backup',

					'.log': 'Logs',
	},
	photos : { 	'.JPG': 'Photos',
				'.png': 'Photos',
				'.jpg': 'Photos',
				'.jpeg': 'Photos',
				'.bmp': 'Photos',

				'.gif': 'Photos',
				'.tiff': 'Photos',
				'.raw': 'Photos',
				'.eps': 'Photos',

				'.xcf': 'Photoshop',
				'.psd': 'Photoshop',
	},	  
	compressed : {	'.jar': 'Compressed',
					'.zip': 'Compressed',
					'.rar': 'Compressed',
					'.tar': 'Compressed',
					'.gz': 'Compressed',
					'.7z': 'Compressed',
					'.bz2': 'Compressed',
	},
	videos : {	'.mp4': 'Videos',
				'.mkv': 'Videos',
				'.flv': 'Videos',
				'.avi': 'Videos', 
	},
	musics : {	'.mp3': 'Music',
				'.ogg': 'Music',
				'.wav': 'Music',   
	},
	others : { '.aux': 'Latex',
				'.dvi': 'Latex',
				'.tex': 'Latex',
				'.dll': 'Windows DLLs',
				'.torrent': 'Torrents'
	}
}






def check_file_ext(source_folder):
	for f in os.listdir(source_folder):
		filename, file_ext = os.path.splitext(f)

def ensure_dir(destination):
	# if not os.path.exists(destination):
	#	os.makedirs(destination)

	for type, dir in types.items():
		path = os.path.join(destination, dir)
		if not os.path.exists(path):
			os.makedirs(path)


def dir_clean(destination):
	files = os.listdir(destination)
	for file in files:
		p = os.path.join(destination, file)
		if os.path.isdir(p) is True:
			includeFiles = os.listdir(p)
			if not includeFiles:
				os.rmdir(p)


def sort_files(source_folder):
	files = os.listdir(source_folder)  # one level file sorting
	for file in files:
		p = os.path.join(source_folder, file)
		if os.path.isdir(p) is True:
			if file not in list(types.values()):
				d = os.path.join(dest, types['directory'])
				try:
					shutil.move(p, d)
					print("Moving {0} to {1}".format(p, d))
				except:
					print("Can`t move {0} to {1}, {2}".format(p, d, sys.exc_info()))
		else:
			ext = os.path.splitext(p)[1]
			if ext in list(types.keys()):  # if types.has_key(ext): deprecated
				d = os.path.join(dest, types[ext])
				try:
					shutil.move(p, d)
					print("Moving {0} to {1}".format(p, d))
				except:
					print("Can`t move {0} to {1}, {2}".format(p, d, sys.exc_info()))
			else:
				print("Leaving {0}".format(p))


def main():
	# Options in sorting
	
	parser = argparse.ArgumentParser(description="Program for file sorting by file extension")
	parser.add_argument("-d", "--destination", dest="destination", help="Directory you want to move files or directories to")
	parser.add_argument("source", help="folder to sort")
	options = parser.parse_args()


	# User define source path or else will be current directory

	if options.source:
		directory = options.source
	else:

	directory = os.getcwd()

	destination = options.destination
	if not os.path.exists(directory):
		print("Invalid directory: {0}".format(directory))
		sys.exit(1)

	if not destination:
		print("Invalid destination")
		sys.exit(1)
	
	# ensure_dir(destination)
	# sort_files(directory, destination, options.recursive)
	# dir_clean(destiantion)

	for type, dir in types.items():
		print (dir)
""" 
# Yes, I'm in the middle of this one, FEELSBADMAN :((((((

def main():
	# Get current directory
	current_dir = os.getcwd()

	for f in os.listdir(current_dir):
		# Split and get files extenstion
		filename, file_ext = os.path.splitext(f)

		try:
			#For each extensions. (Need to improve when I have time, need to keep it DRY man)
			if not file_ext:
				pass

			elif file_ext in ('.exe', '.air', '.msi', '.rpm', '.dmg', '.apk', '.swf', '.iso'):
				if os.path.exists(current_dir+'/'+'Programs'):
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Programs', f'{filename}{file_ext}'))
				else:
					os.makedirs(current_dir+'/'+'Programs')
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Programs', f'{filename}{file_ext}'))

			elif file_ext in ('.ppt', '.doc', '.docx', '.dotx.xls', '.xlsx', '.pdf', '.txt', '.xml', '.htm', '.html'):
				if os.path.exists(current_dir+'/'+'Documents'):
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Documents', f'{filename}{file_ext}'))
				else:
					os.makedirs(current_dir+'/'+'Documents')
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Documents', f'{filename}{file_ext}'))


			elif file_ext in ('.jpg', '.png', '.gif', '.jpeg', '.bmp', '.tiff', '.raw', '.eps', '.xcf', '.psd'):
				if os.path.exists(current_dir+'/'+'Photos'):
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Photos', f'{filename}{file_ext}'))
				else:
					os.makedirs(current_dir+'/'+'Photos')
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Photos', f'{filename}{file_ext}'))

			elif file_ext in ('.jar', '.zip', '.rar', '.tar', '.gz', '.7z', '.bz2'):
				if os.path.exists(current_dir+'/'+'Compressed'):	
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Compressed', f'{filename}{file_ext}'))
				else:
					os.makedirs(current_dir+'/'+'Compressed')
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Compressed', f'{filename}{file_ext}'))

			elif file_ext in ('.mp4', '.mkv', '.flv', '.avi', '.webp'):
				if os.path.exists(current_dir+'/'+'Videos'):
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Videos', f'{filename}{file_ext}'))
				else:
					os.makedirs(current_dir+'/'+'Videos')
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Videos', f'{filename}{file_ext}'))

			elif file_ext in ('.mp3', '.ogg', '.wav'):
				if os.path.exists(current_dir+'/'+'Musics'):
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Musics', f'{filename}{file_ext}'))
				else:
					os.makedirs(current_dir+'/'+'Musics')
					shutil.move(
						os.path.join(current_dir, f'{filename}{file_ext}'),
						os.path.join(current_dir, 'Musics', f'{filename}{file_ext}'))

	# I'm just violating DRY so much Haha, I just don't even care anymore D: Soon tho :|
		except (FileNotFoundError, PermissionError):
			pass


if __name__ == "__main__":
	main()