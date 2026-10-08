"""Bitmap Message, by Cory R. Black (Cory.r.black@icloud.com)
Displays a text message according to the provided bitmap image."""

import sys

bitmap = """
..................................................................................

********  ***    **  ********    ********  ********  ********  ********  ********
**    **  ****   **  **          **    **  ********  **        ********  **
**    **  ** **  **  ****        ********     **     ****      **        ****
**    **  **  ** **  **          **           **     **        **        **
**    **  **   ****  **          **        ********  **        ********  **
********  **    ***  ********    **        ********  ********  ********  ********

.................................................................................."""

print('Bitmap Message, by Cory R. Black (Cory.r.black@icloud.com)')
print('Enter the message to display with the bitmap')
message = input('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()
