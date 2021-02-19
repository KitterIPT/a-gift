import os
import shutil
# A small gift for you. Happy birthday, Phuong. Hope it brings you joy :) This feels a bit cringy haha, whatever.
"""
	Descriptions: 	Sorting scripts base on file extension.
	Version: 		0.1.2
	Author: 		KitterIPT
	Date_Created:	17/02/2021
	Date_Modified:	19/02/2021
	======================================
	Format: 	1) noun_obj
				2) obj_verb
				3) obj for an object, obj(s) for list of objects
	======================================
	NTBD:	* Data serialization (JSON or YAML - prefer YAML).
			* Source and Destination directory.
			* SysInfo using sys.exc_info().
			* Applying decorator and such.
			* What's deprecated and recursive.
			* User Interface - GUI (PyQt, Tkinter, wxPython).
				/or Scripting options (argparser).
"""


# Dict for which file go to what folder: (file_extension : folder) 
# Will be using YAML for this soon, not JSON tho. Would like to use DB but I guess not.
types = {
	'.application': 'Programs',
	'.exe': 'Programs',
	'.air': 'Programs',
	'.msi': 'Programs',
	'.rpm': 'Programs',
	'.dmg': 'Programs',

	'.swf': 'Programs',
	'.apk': 'Programs',
	'.iso': 'Programs',
	
	'.pptx': 'Documents', #'Powerpoints',
	'.ppt': 'Documents', #'Powerpoints',

	'.doc': 'Documents', #'Words',
	'.docx': 'Documents', #'Words',
	'.dotx': 'Documents', #'Words',

	'.xls': 'Documents', #'Excels',
	'.xlsx': 'Documents', #'Excels',	

	'.pdf': 'Documents', #'PDFs',

	'.xml': 'Documents', #'Web',
	'.htm': 'Documents', #'Web',
	'.html': 'Documents', #'Web',
	
	'.odp': 'Documents',
	'.wbk': 'Documents',
	'.odt': 'Documents',

	'.txt': 'Documents', #'Text',
	'.mht': 'Documents', #'Text',

	'.epub': 'Documents', #'Books',
	'.fb2': 'Documents', #'Books',
	'.mobi': 'Documents', #'Books',
	'.djvu': 'Documents', #'Books',

	'.odb': 'Documents', #'Databases',
	'.mwb': 'Documents', #'Databases',
	'.sql': 'Documents', #'Databases',
	'.sql.gz': 'Documents', #'Databases',
	'.tgz': 'Documents', # 'Databases',
	'.tar.gz': 'Documents', #'Databases',
	'.csv': 'Documents', #'Databases',

	'.jnlp': 'Documents', #'Scripts',
	'.c': 'Documents', #'Scripts',
	'.sh': 'Documents', #'Scripts',
	'.py': 'Documents', #'Scripts',
	'.phtml': 'Documents', #'Scripts',
	'.php': 'Documents', #'Scripts',
	'.aspx': 'Documents', #'Scripts',
	'.pl': 'Documents', #'Scripts',
	'.js': 'Documents', #'Scripts',

	'.bak': 'Documents', #'Backup',
	'.bk': 'Documents', #'Backup',

	'.log': 'Documents', #'Logs',
	
	'.png': 'Photos',
	'.jpg': 'Photos',
	'.jpeg': 'Photos',
	'.bmp': 'Photos',

	'.gif': 'Photos',
	'.tiff': 'Photos',
	'.raw': 'Photos',
	'.eps': 'Photos',

	'.xcf': 'Photos', #'Photoshop',
	'.psd': 'Photos', #'Photoshop',
	
	'.jar': 'Compressed',
	'.zip': 'Compressed',
	'.rar': 'Compressed',
	'.tar': 'Compressed',
	'.gz': 'Compressed',
	'.7z': 'Compressed',
	'.bz2': 'Compressed',
	
	'.mp4': 'Videos',
	'.mkv': 'Videos',
	'.flv': 'Videos',
	'.avi': 'Videos', 

	'.mp3': 'Music',
	'.ogg': 'Music',
	'.wav': 'Music', 

	'.aux': 'Others', #'Latex',
	'.dvi': 'Others', #'Latex',
	'.tex': 'Others', #'Latex',

	'.dll': 'Others', #'Windows DLLs',

	'.torrent': 'Others', #'Torrents'
}


# Moving files from source folder to each folder type using file_extension.
def file_move(source_dir, destination_dir, dir_type, file):
	shutil.move(
			os.path.join(source_dir, file),
			os.path.join(destination_dir, dir_type, file)
	)


""" I guess we don't really need this.
def dir_check(source_dir, dir_type):
	real_path = source_dir + '/' + dir_type

	if os.path.exists(real_path):
		os.makedirs(real_path)
"""


# Main sorting alg.
def file_sort(source_dir, destination_dir):
	# Path announcement
	print("[FILE SORTING]")
	print("Source Directory: {0}\nDestination Directory: {1}".format(source_dir, destination_dir))
	print("================")

	# Go through each file one by one.
	for f in os.listdir(source_dir):
		# Split and get files extenstion.
		name_file, ext_file = os.path.splitext(f)

		try:
			# Make an axception for this file.
			if f == 'main.py':
				pass

			# File does not have extension.
			elif not ext_file:
				pass
				#print("File {} doesn`t have extension.".format(f))

			# File does have extension.
			else:
				# Go through each key in types_dict.
				# Python automatically __iter__() through key if put dict directly.
				for k in types:
					if ext_file == k:
						# Real path for each type.
						real_destination_path = destination_dir + '\\' + types[k]

						# Check if there's already a directory for this type.
						if os.path.exists(real_destination_path):
							file_move(source_dir, destination_dir, types[k], f)
							print("Moved file {0} from [SourceDirectory] to folder {1} in [DestinationDirectory].".format(f, types[k]))
						else:
							# Create one if there isn't and moving the file.
							os.makedirs(real_destination_path)
							print("Created folder {0} in [DestinationDirectory].".format(types[k]))
							file_move(source_dir, destination_dir, types[k], f)

		# No permisson.
		except (FileNotFoundError, PermissionError):
			print("Do not have Permisson to move {0}".format(f))


# For when running script directly.
def script_stop():
	input("Press any key to continute.\n")


def main():
	# Get current directory.
	# Will be change soon that you can put directory's path in, destination directory as well.
	current_dir = os.getcwd()

	file_sort(current_dir, current_dir)

	script_stop()

if __name__ == "__main__":
	main()