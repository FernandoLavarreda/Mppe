# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
# Multi Purpose Py Edit
# Free software
import sys
import parsing

if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(parsing.run(*parsing.parse_entry(arguments)))