#! python3
# mclip.py - A multi-clipboard program.

import sys, pyperclip

TEXT = {
    'reopen' : 
"""
Hi,

The service report has been reopened.
You can go on working on it.

BR
"""
}

# Falls kein Argument vorhanden ist, quitiere das Programm
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]     # Gibt das erste Argument wieder, was im Terminal nach dem File-Name eingegeben wurde

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}')