# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Parse User commands"""
from . import tools, shell, editor

# Set of executable commands (aliases for command, command) : (lower-arg-limit,upper-arg-limit,ends-with-multi-args,command-to-execute)
ACCEPTED = {("-e", "-editor") : (0, 1, False, editor.run),
            ("-h", "-help") : (0, 0, False, tools.help_),
            ("-s", "-shell") : (0, 0, False, shell.run),
            ("-ls", "-list") : (1, 2, True, tools.view_files), 
            ("-c", "-compare") : (2, 4, True, tools.compare_dir),
            ("-t", "-transfer") : (2, 4, True, tools.transfer_files),
            ("-r", "-read") : (1, 1, False, tools.read),
            ("-rm", "-remove") : (1, 2, True, tools.remove),
            }

def parse_entry(tokens_):
    """Read arguments from the commandline, validate they are recognized commands with a set of arguments
    corresponding to the inclusive interval set in ACCEPTED"""
    tokens = [t.lower() for t in tokens_]
    valid = []
    for token in ACCEPTED.keys():
        valid+=token
    if tokens[0] not in valid:
        if len(tokens)>1:
            return "Too many arguments", ()
        else:
            return tokens, ("-e", "-editor")
    else:
        position = valid.index(tokens[0])
        if position %2 != 0:
            key = (valid[position-1], valid[position])
        else:
            key = (valid[position], valid[position+1])
        if len(tokens)-1>=ACCEPTED[key][0] and len(tokens)-1<= ACCEPTED[key][1]:
            return tokens[1:], key
        else:
            return "Incorrect number of arguments", ()

def run(tokens, key):
    """Run command, separating last arg into varios args acording to ACCPETED[key][3] if required"""
    if key:
        if ACCEPTED[key][2]:
            if len(tokens)==ACCEPTED[key][1]:
                final_input = tokens[:-1]
                final_input.append(tokens[-1].split(" "))
            else:
                final_input = tokens[:]
        else:
            final_input = tokens[:]
        try:
            return(ACCEPTED[key][3](*final_input))
        except TypeError:
            return "Shell closed"
    else:
        return (tokens)

if __name__ == "__main__":
    pass