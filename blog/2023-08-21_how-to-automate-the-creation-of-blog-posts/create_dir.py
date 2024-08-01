import os 
import sys
from datetime import datetime
import shutil

def create_post(type_file, post_name):

    # Save a copy only name
    raw_post_name = post_name

    # Example: "how-to-rock"
    post_name = post_name.lower().replace(" ", "-")

    # Current Date: "2023-08-29"
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Folder name: "2023-08-29_how-to-rock"
    folder_name = current_date + '_' + post_name

    # Current Directory path
    current_dir = os.getcwd()
    
    # Output Directory
    output_path = current_dir + "/out"

    # Folder Path: "../out/2023-08-29_how-to-rock"
    path_folder = os.path.join(output_path, folder_name)

    # Make a Directory
    os.mkdir(path_folder)
    # print("Directory '% s' created!" % folder_name)

    # --------------- HELPER FUNCTION ------------------

    def create_file(type_file):

        # -------------- CREATE FILE --------------
        # Holds available extensions
        dic = {'post': 'qmd', 'poems':'qmd', 'notebook':'ipynb', 'note':'md'}
        file_extension = dic[type_file]
        
        # Source path: "../template/file_type/index.ext"
        source_file = f"templates/{type_file}/index.{file_extension}"
        
        # File name "index.ext"
        file_name = f"index.{file_extension}"

        # Destination path: "../out/2023-08-29_how-to-rock/index.ext"
        destination_file = os.path.join(path_folder, file_name)

        # Creating a Copy from Template folder
        shutil.copy(source_file, destination_file)


        # -------------- UPDATE HEADER --------------
        lines = open(destination_file, 'r').readlines()
        
        if (type_file == "notebook"):
            title_row = 9
            lines[title_row] = f'    \"title: \\"{raw_post_name.capitalize()}\\"\\n\",'

            date_row = 11
            lines[date_row] = f'    \"date: \\"{current_date}\\"\\n\",'

            code_name_row = 16
            post_code_name = post_name + '.out.ipynb'
            lines[code_name_row] = f'    \"      file-name: {post_code_name}\\n\",'

        else:
            title_row = 1
            lines[title_row] = f'title: "{raw_post_name.capitalize()}"\n'

            date_row = 3
            lines[date_row] = f'date: "{current_date}"\n'

        file = open(destination_file, 'w')
        file.writelines(lines)
        file.close()

        # -------------- MOVE FILE --------------
        # Folder Path: "../out/2023-08-29_how-to-rock"
        src = path_folder

        # Path to Blog or Notes
        if (type_file == 'note' ):
            dst = "../../notes"
            print(f"notes/{folder_name}/")
        else: 
            dst = "../../blog"
            print(f"blog/{folder_name}/")

        # Move the file from out/ folder    
        shutil.move(src, dst)     


    # Detect the type of file to be created
    if (type_file == "post"):
        create_file("post")
    elif (type_file == "notebook"):
        create_file("notebook")
    elif (type_file == "poems"):
        create_file("poems")
    elif (type_file == "note"):
        create_file("note")
    else:
        print(f"Wrong type_file: {type_file}. Available: 'post', 'poems', 'notebook' or 'note'")
        sys.exit()


if __name__ == "__main__":

    # 0 is the name of the py file
    # 1 is the first argument
    type_file = sys.argv[1]
    post_name = sys.argv[2]

    create_post(type_file, post_name)