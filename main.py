import os
import shutil
# A small gift for you. Happy birthday, Phuong. Hope it brings you joy :) A bit cringy haha, whatever.
"""
	# Format: 	1) noun_obj
				2) obj_verb
				3) obj for an object, obj(s) for list of objects
"""

types = {
	# Dict for which file go to what folder: (file_extension : folder) 
	# Will be using YAML for this soon, not JSON tho. Would like to use DB but I guess not.
	'.application': 'Programs',
	'.exe': 'Programs',
	'.air': 'Programs',
	'.msi': 'Programs',
	'.rpm': 'Programs',
	'.dmg': 'Programs',

	'.swf': 'Programs',
	'.apk': 'Programs',
	'.iso': 'Programs',
	
	'.pptx': 'Documents', # 'Powerpoints',
	'.ppt': 'Documents', #'Powerpoints',

	'.doc': 'Documents', # 'Words',
	'.docx': 'Documents', # 'Words',
	'.dotx': 'Documents', # 'Words',

	'.xls': 'Documents', # 'Excels',
	'.xlsx': 'Documents', # 'Excels',	

	'.pdf': 'Documents', # 'PDFs',

	'.xml': 'Documents', # 'Web',
	'.htm': 'Documents', # 'Web',
	'.html': 'Documents', # 'Web',
	
	'.odp': 'Documents',
	'.wbk': 'Documents',
	'.odt': 'Documents',

	'.txt': 'Documents', # 'Text',
	'.mht': 'Documents', # 'Text',

	'.epub': 'Documents', # 'Books',
	'.fb2': 'Documents', # 'Books',
	'.mobi': 'Documents', # 'Books',
	'.djvu': 'Documents', # 'Books',

	'.odb': 'Documents', # 'Databases',
	'.mwb': 'Documents', # 'Databases',
	'.sql': 'Documents', # 'Databases',
	'.sql.gz': 'Documents', # 'Databases',
	'.tgz': 'Documents', # 'Databases',
	'.tar.gz': 'Documents', # 'Databases',
	'.csv': 'Documents', # 'Databases',

	'.jnlp': 'Documents', # 'Scripts',
	'.c': 'Documents', # 'Scripts',
	'.sh': 'Documents', # 'Scripts',
	'.py': 'Documents', # 'Scripts',
	'.phtml': 'Documents', # 'Scripts',
	'.php': 'Documents', # 'Scripts',
	'.aspx': 'Documents', # 'Scripts',
	'.pl': 'Documents', # 'Scripts',
	'.js': 'Documents', # 'Scripts',

	'.bak': 'Documents', # 'Backup',
	'.bk': 'Documents', # 'Backup',

	'.log': 'Documents', # 'Logs',
	
	'.png': 'Photos',
	'.jpg': 'Photos',
	'.jpeg': 'Photos',
	'.bmp': 'Photos',

	'.gif': 'Photos',
	'.tiff': 'Photos',
	'.raw': 'Photos',
	'.eps': 'Photos',

	'.xcf': 'Photos', # 'Photoshop',
	'.psd': 'Photos', # 'Photoshop',
	
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

	'.aux': 'Others', # 'Latex',
	'.dvi': 'Others', # 'Latex',
	'.tex': 'Others', # 'Latex',

	'.dll': 'Others', # 'Windows DLLs',

	'.torrent': 'Others', #'Torrents'
}


def file_move(source_dir, name_file, ext_file, dir_type):
	# Moving files from source folder to each folder type using file_extension.
	file = f'{name_file}{ext_file}'

	shutil.move(
			os.path.join(source_dir, file),
			os.path.join(source_dir, dir_type, file)
	)


"""I guess we don't really need this.
def dir_check(source_dir, dir_type):
	real_path = source_dir + '/' + dir_type

	if os.path.exists(real_path):
		os.makedirs(real_path)
"""


def main():
	# Get current directory.
	# Will be change that you can put directory's path in, destination directory as well.
	current_dir = os.getcwd()

	# Go through each file one by one.
	for f in os.listdir(current_dir):
		# Split and get files extenstion.
		name_file, ext_file = os.path.splitext(f)

		try:
			if not ext_file:
				# File have no extension.
				pass

			else:
				# File have extension.
				for k in types:
					# Go through each key in types_dict.
					# Python automatically __iter__() through key if put dict directly.
					if ext_file == k:
						real_path = current_dir + '/' + types[k]

						if os.path.exists(real_path):
							# Check if there's already a directory for this type.
							file_move(current_dir, name_file, ext_file, types[k])
						else:
							# Create one if there isn't and moving the file.
							os.makedirs(real_path)
							file_move(current_dir, name_file, ext_file, types[k])

		except (FileNotFoundError, PermissionError):
			pass


if __name__ == "__main__":
	main()