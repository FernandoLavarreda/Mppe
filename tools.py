# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Multiple file functionalities"""

import os
import time
import shutil

def compare_dir(dir1, dir2, detailed=False, file_extensions=()):
    """Compare the contents in two directories, output into a file.
    Provide two paths followed by boolean of text in depth description and file extentions"""
    if os.path.exists(dir1) and os.path.isdir(dir1):
        if os.path.exists(dir2) and os.path.isdir(dir2):
            shared = []
            unique1 = []
            unique2 = []
            files_dir1 = list_files(dir1, file_extensions)
            files_dir2 = list_files(dir2, file_extensions)
            
            for file in files_dir1:
                if file in files_dir2:
                    shared.append(file)
                else:
                    unique1.append(file)
            for file in files_dir2:
                if file not in shared:
                    unique2.append(file)
            return format_compare(dir1, dir2, unique1, unique2, shared, detailed)
        else:
            return "ERROR\nPath: "+dir2+" NOT FOUND"
    else:
        return "ERROR\nPath: "+dir1+" NOT FOUND"

def list_files(folder, file_extensions=()):
    """See the content in a directory"""
    content = []
    if folder == ".":
        folder = os.getcwd()
    with os.scandir(folder) as fd:
                    for file in fd:
                        if file_extensions:
                            if file.is_file() and file.name[file.name.find("."):] in file_extensions:
                                content.append(file.name)
                        else:
                            content.append(file.name)
    return content

def view_files(files):
    """Printing all content in a list"""
    for  fd in files:
        print(fd)

def format_compare(dir1, dir2, d1_files, d2_files, shared, detailed):
    """Improve information presented in compare"""
    formatted = dir1+" unique files: "+str(len(d1_files))+"\n"+dir2+" unique files: "+str(len(d2_files))+"\nShared files: "+str(len(shared))
    if detailed:
        for fd in range(len(d1_files)):
            d1_files[fd] = d1_files[fd]+"\n"
        for fd in range(len(d2_files)):
            d2_files[fd] = d2_files[fd]+"\n"
        for fd in range(len(shared)):
            shared[fd] = shared[fd]+"\n"
        with open("detailed.txt", "w") as dt:
            dt.write(formatted)
            dt.write("\n\nShared:\n")
            dt.writelines(shared)
            dt.write("\n\n"+dir1+" unique: " +"\n")
            dt.writelines(d1_files)
            dt.write("\n\n"+dir2+" unique:" +"\n")
            dt.writelines(d2_files)
        os.startfile(os.getcwd()+"\\detailed.txt")
        return "Success."
    else:
        return formatted

def transfer_files(dir1, dir2, interval=10, file_extensions=()):
    """Transfer information from a folder to another for an specified time
        Option to limit the file extensions to pass"""
    if os.path.exists(dir1) and os.path.isdir(dir1):
        if os.path.exists(dir1) and os.path.isdir(dir1):
            start = time.perf_counter()
            trasnfered = []
            while time.perf_counter()-start<interval:
                try:
                    contents = list_files(dir1, file_extensions)
                    for content in contents:
                        if content not in trasnfered:
                            trasnfered.append(content)
                            shutil.copy(dir1+"\\"+content, dir2)
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    return "An ERROR ocurred: "+str(e)
        else:
            return "Error\nPath: "+dir2+" NOT FOUND"
    else:
        return "Error\nPath: "+dir1+" NOT FOUND"
    return "Execution Ended"


if __name__ == "__main__":
    pass