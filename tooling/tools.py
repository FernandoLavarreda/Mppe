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

def view_files(folder, file_extensions=()):
    """Printing all content in a list"""
    if os.path.isdir(folder):
        files = list_files(folder, file_extensions)
        reading = ""
        for  fd in files:
            reading += fd+"\n"
        return reading
    else:
        return "No such directory"

def format_compare(dir1, dir2, d1_files, d2_files, shared, detailed):
    """Improve information presented in compare"""
    formatted = dir1+" unique files: "+str(len(d1_files))+"\n"+dir2+" unique files: "+str(len(d2_files))+"\nShared files: "+str(len(shared))
    if detailed == "y" or detailed == "yes":
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

def transfer_files(dir1, dir2, interval_="10", file_extensions=()):
    """Transfer information from a folder to another for an specified time
        Option to limit the file extensions to pass"""
    try:
        interval = int(interval_)
    except Exception:
        return "Non numeric value passed to interval"
    else:
        if os.path.exists(dir1) and os.path.isdir(dir1):
            if os.path.exists(dir1) and os.path.isdir(dir1):
                start = time.perf_counter()
                trasnfered = []
                print("Process started. Press ctrl+c to stop before timer")
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

def remove(folder, file_extensions=()):
    """Delete a path given"""
    if os.path.isfile(folder):
        try:
            os.remove(folder)
        except Exception:
            return "Not able to remove file"
    elif os.path.isdir(folder):
        if file_extensions and "*" not in file_extensions:
            content = list_files(folder, file_extensions)
            for ct in content:
                try:
                    os.remove(folder+"\\"+ct)
                except Exception:
                    return "Not able to remove file"
        elif file_extensions:
            content = list_files(folder)
            for ct in content:
                try:
                    os.remove(folder+"\\"+ct)
                except Exception:
                    return "Not able to remove file"
        else:
            try:
                shutil.rmtree(folder)
            except Exception:
                return "Not able to remove folder"
    else:
        return("Error\nPath: "+folder+" NOT FOUND")
    return "Path removed successfully"

def read(path):
    """Read a text file and print it to console"""
    try:
        with open(path, "r") as rd:
            return rd.read()
    except FileNotFoundError:
        return "File Not Found"
    except Exception:
        return "An Error ocurred."

def help_():
    """Basic introduction to the program"""
    info = """Welcome to Multi Purpose Py Edit:
    Commands                        Arguments                                               Description
    -s  -shell                                                                              Open interactive shell
    -h  -help                                                                               See commands and description
    -e  -editor                             optional: 'path'                                Open editor with given file if provided
    -ls -list       'path'                  optional: '.extension1 .extension2 ...'         List contents of path . to refer to cwd. Option to provide file ext
    -c  -compare    'path1' 'path2'         optional: 'detailed' '.ext1 .ext2 ...'          Compare contents between two files
    -t  -transfer   'path1' 'path2'         optional: 'int' '.ext1 .ext2 ...'               Copy specified content from path1 to path2 during 'int' time(default 3s). 
    -r  -read       'path'                                                                  Read contents of text file
    -rm -remove     'path'                  optional: '.ext1 .ext2'                         Remove given path if extensions given only those files"""
    return info

if __name__ == "__main__":
    pass