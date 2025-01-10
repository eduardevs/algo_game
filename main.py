import time
from pathlib import Path
import shutil
import os
import subprocess
import progressbar

def copy_rename_pathlib(src_path, dest_path, new_name):
    src_path = Path(src_path).resolve()
    dest_path = Path(dest_path).resolve()

    # Ensure the destination directory exists
    dest_path.mkdir(parents=True, exist_ok=True)

    # Create the new full path for the destination file
    new_path = dest_path / new_name

    # Copy the file to the new location with the new name
    shutil.copy2(src_path, new_path)

    # Explicitly flush file system buffers to ensure the file is fully written
    with open(new_path, 'r') as f:
        os.fsync(f.fileno())

    # Change the current working directory to the destination path
    os.chdir(dest_path)

    print(f"File copied successfully to {new_path}")

    # Simulate a charging period with progressbar
    print("Charging... Please wait.")
    widgets = ['[', progressbar.Percentage(), '] ', progressbar.Bar()]
    bar = progressbar.ProgressBar(widgets=widgets, maxval=10)
    bar.start()
    for i in range(5):
        time.sleep(0.5)  # Simulate delay
        bar.update(i+1)
    bar.finish()

    print("\nOpening file with vim...\n")
    
    # Open the new file with vim
    subprocess.run(['vim', str(new_path)])

def create_algo():
    algo_name = input("which algo name ?")
    algo_name = f"{algo_name}.py"
    copy_rename_pathlib('./template.py', './play/algorithmes', algo_name )

def create_ds():
    ds_name = input("which data structure name ?")
    ds_name = f"{ds_name}.py"
    copy_rename_pathlib('./template.py', './play/data-structures', ds_name)

    

def start_game():
    
    while(True):
        print("Welcome to the algorithms game \n choice an option \n 1. Create an algo \n 2. Create data structure \n")
        choice = input("Select an option to start")
        if choice == "1":
            create_algo()
            break

        elif choice == "2":
            create_ds()
            break


def main():
    start_game()
    

if __name__ == "__main__":
    main()
