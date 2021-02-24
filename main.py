import os
import shutil
import yaml


# A small gift for you. Happy birthday, Phuong. Hope it brings you joy :) This feels a bit cringy haha, whatever.
"""
	Descriptions: 	Sorting scripts base on file extension.
	Version: 		0.1.2.1
	Author: 		KitterIPT
	Date_Created:	17/02/2021
	Date_Modified:	24/02/2021
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


class FileProcess():
	@staticmethod
	def yaml_load(yaml_path):
		with open(yaml_path) as file:
			yaml_dict = yaml.load(file, Loader=yaml.FullLoader)
		return yaml_dict


class FileSorting():
	def __init__(self, src_dir, dst_dir, types_dict):
		self.source_dir = src_dir
		self.destination_dir = dst_dir
		self.types_dict = types_dict

	# Moving files from source folder to each folder type using file_extension.
	def file_move(self, dir_type, file):
		shutil.move(
				os.path.join(self.source_dir, file),
				os.path.join(self.destination_dir, dir_type, file)
		)
		print("Moved file {0} from [SourceDirectory] to folder {1} in [DestinationDirectory].".format(file, dir_type))

	def sorted_move(self, extension, file):
		# Go through each key in types_dict.
		# Python automatically __iter__() through key if put dict directly.
		for key in self.types_dict: 
			if extension == key:
				# Real path for each type.
				real_destination_path = self.destination_dir + '\\' + self.types_dict[key]

				# Check if there's already a directory for this type.
				if os.path.exists(real_destination_path):
					self.file_move(self.types_dict[key], file)
					
				else:
					# Create one if there isn't and moving the file.
					os.makedirs(real_destination_path)
					print("Created folder {0} in [DestinationDirectory].".format(self.types_dict[key]))
					self.file_move(self.types_dict[key], file)

	# Main sorting alg.
	def file_sort(self):
		# Path announcement
		print("[FILE SORTING]")
		print("Source Directory: {0}\nDestination Directory: {1}".format(self.source_dir, self.destination_dir))
		print("================")

		# Go through each file one by one.
		for f in os.listdir(self.source_dir):
			# Split and get files extenstion.
			name_file, ext_file = os.path.splitext(f)

			try:
				# Make an axception for this file.
				if f == 'main.py':
					pass

				elif f == 'KitterIPT':
					print("Yo. Guess who's back. Back again. Kitter`s back. Tell a friend.\n")

				# File does not have extension.
				elif not ext_file:
					pass
					#print("File {} doesn`t have extension.".format(f))

				# File does have extension. 
				else:
					self.sorted_move(ext_file, f)
					

			# No permisson.
			except (FileNotFoundError, PermissionError):
				print("Do not have Permisson to move {0}".format(f))


# For when running script directly. Only with no additional package from virtual environment.
def screen_pause():
	input("Press any key to continute.\n")


def main():
	# Get current directory.
	# Will be change soon that you can put directory's path in, destination directory as well.
	current_dir = os.getcwd()
	yaml_path = current_dir + '\\' + 'types.yaml'
	types = FileProcess.yaml_load(yaml_path)

	sorting = FileSorting(current_dir, current_dir, types)
	
	sorting.file_sort()


if __name__ == "__main__":
	main()