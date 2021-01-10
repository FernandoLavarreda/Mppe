# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Shell to interact with Multi Purpose Py Edit"""
import cmd
import time
import tools

ACCEPTED = {"compare" : (2, 4, True, tools.compare_dir),
            "transfer" : (2, 4, True, tools.transfer_files),
            "list" : (1, 2, True, tools.view_files),
            "remove" : (1, 2, True, tools.remove),
            "read" : (1, 1, False, tools.read),
            }

def parse(key, args_):
    if args_.count("'")>0 and args_.count("'")%2==0:
        args = args_.split("'")
        args.pop(0)
        args.pop(-1)
        while " " in args:
            args.remove(' ')
    else:
        print("Not a valid entry")
        return ""
    if len(args) >= ACCEPTED[key][0] and len(args) <= ACCEPTED[key][1]:
        if ACCEPTED[key][2] and len(args) == ACCEPTED[key][1]:
            final_input = args[:-1]
            final_input.append(args[-1].split(" "))
            print(ACCEPTED[key][3](*final_input))
        else:
            print(ACCEPTED[key][3](*args))
    else:
        print("Incorrect number of arguments")

class Mppe(cmd.Cmd):
    intro = "Welcome to Multi Purpose Py Edit. Type help to list commands. To exit press ctrl+c.\nArguments in shell sep using: ''"
    prompt = "&> "

    def do_compare(self, arg):
        """Compare the files between two folders, may specify certain extensions and detailed to show comparisons:
           &> compare 'path1' 'path2' 'detailed ('yes' or 'y' else no detalied description)' '.ext1 .ext2 .ext3' """
        parse("compare", arg)

    def do_list(self, arg):
        """List the files in a directory use '.' for shortcut to current folder file extentions are optional: 
        &> list 'path1' '.ext1 .ext2' """
        parse("list", arg)
    
    def do_transfer(self, arg):
        """Transfer (copy) files from one directory to another. Optional to set time in seconds (default is 3) and file extentions: 
        &> transfer 'path1' 'path2' '10' '.ext1 .ext2' """
        parse("transfer", arg)
    
    def do_remove(self, arg):
        """Remove a file or directory: &> remove 'path' """
        parse("remove", arg)

    def do_read(self, arg):
        """See contents from a text file: &> read 'path' """
        parse("read", arg)

    def precmd(self, line):
        line = line.lower()
        return line

def run():
    try:
        Mppe().cmdloop()
    except KeyboardInterrupt:
        return "Shell closed"

if __name__ == "__main__":
    run()