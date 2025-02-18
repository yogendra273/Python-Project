#importing the files
import os
import shutil
import datetime

#function to backup files
def backup_files(source_dir, destination_dir):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_dir = os.path.join(destination_dir, f"backup_{timestamp}")

    try:
        shutil.copytree(source_dir, backup_dir)
        print(f"Backup created successfully at {backup_dir}")
    except OSError as e:
        print(f"Error creating backup: {e}")


if __name__ == "__main__":
    source_directory = "C:/Users/pc/Desktop/Data Science/Bank Customer Churn Prediction"
    destination_directory = "C:/Users/pc/Desktop/Destination"

    backup_files(source_directory, destination_directory)


