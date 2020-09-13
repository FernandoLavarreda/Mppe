# Fernando José Lavarreda Urizar
# fernandolavarredau@gmail.com
"""Parse User commands"""
import re

ACCEPTED = {("-s", "-shell") : (0),
            ("-ls") : (0, 1), 
            ("-c", "-compare") : (4),
            ("-t", "-transfer") : (3),
            }