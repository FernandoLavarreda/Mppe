# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
# Multi Purpose Py Edit
# Free software
import sys
from tooling import parsing

if __name__ == "__main__":
    if len(sys.argv)>1:
        arguments = sys.argv[1:]
        print(parsing.run(*parsing.parse_entry(arguments)))