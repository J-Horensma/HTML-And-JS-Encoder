import sys, time, signal, base64, click, pyperclip
from Encoding_Libraries.HTML_entity_names import *
from Encoding_Libraries.HTML_decimal_entities import *
from Encoding_Libraries.HTML_hex_entities import *
from Encoding_Libraries.unicode_escape import *
from Encoding_Libraries.unicode_code_point_escape import *
from Encoding_Libraries.hex_escape import *
from Encoding_Libraries.octal_escape import *
from Encoding_Libraries.URL_encoding import *
    
def choose_encoding_type():
    while True:
        click.clear()
        print('HTML And JS Encoder')
        print('-------------------\n')
        ENCODING_OPTIONS = ['HTML Entity Names', 'Decimal HTML Entities', 'Hex HTML Entites', 'Unicode Escape', 'Unicode Code-Point Escape', 'Hex Escape','Octal Escape', 'base64 encoding', 'URL encoding']
        i = 1
        for VALUE in ENCODING_OPTIONS:
            print(f'{i}.) {VALUE}')
            i += 1
        ENCODING_CHOICE = input(f'\nChoose an encoding type (1-{(i - 1)}): ')

        if ENCODING_CHOICE == '1':
            DICTIONARY = HTML_ENTITY_NAMES
            return DICTIONARY
        elif ENCODING_CHOICE == '2':
            DICTIONARY = DECIMAL_HTML_ENTITIES
            return DICTIONARY
        elif ENCODING_CHOICE == '3':
            DICTIONARY = HEX_HTML_ENTITIES
            return DICTIONARY
        elif ENCODING_CHOICE == '4':
            DICTIONARY = UNICODE_ESCAPE
            return DICTIONARY
        elif ENCODING_CHOICE == '5':
            DICTIONARY = UNICODE_CODE_POINT_ESCAPE
            return DICTIONARY
        elif ENCODING_CHOICE == '6':
            DICTIONARY = HEX_ESCAPE
            return DICTIONARY
        elif ENCODING_CHOICE == '7':
            DICTIONARY = OCTAL_ESCAPE
            return DICTIONARY
        elif ENCODING_CHOICE == '8':
           INPUT = multiline_input()
           INPUT_BYTES = INPUT.encode('utf-8')
           BASE64_BYTES = base64.b64encode(INPUT_BYTES)
           BASE64_STRING = BASE64_BYTES.decode('utf-8')
           click.clear()
           print('Encoded String:\n')
           print(BASE64_STRING,'\n')
           input('Press Enter: ')
        elif ENCODING_CHOICE == '9':
            DICTIONARY = URL
            return DICTIONARY
        else:
            print(f'Input must be a number, in range of the above options')
            input('Press Enter: ')
            continue

def close_sys_stdin(signum, frame):
    return

def multiline_input():
    while True:
        click.clear()
        signal.signal(signal.SIGINT, close_sys_stdin)
        print('1.) Type or paste a script, below')
        print('2.) Press "Enter", to ensure the last line registers')
        print('3.) Press "ctrl" + "C" to continue):\n')
        LINES = ''.join(sys.stdin.read()).strip()
        if LINES.strip():
            break
        else:
            print('Input, cannot be empty')
            input('Press Enter: ')
            continue
    return LINES

def exit(signum, frame):
    click.clear()
    print('Exiting...')
    time.sleep(1)
    exit()

def encode_string(DICTIONARY):
        INPUT = multiline_input()
        signal.signal(signal.SIGINT, exit)
        print('Enter a list of characters/continuous strings (Separated by spaces)')
        EXCLUDED_CHARACTERS = list(input('Format: alert confirm prompt ( ): '))
        ENCODED_STRING = ''
        for CHARACTER in INPUT:
            if CHARACTER in DICTIONARY and CHARACTER not in EXCLUDED_CHARACTERS:
                CHARACTER = DICTIONARY[CHARACTER]
            ENCODED_STRING = ENCODED_STRING + CHARACTER
        click.clear()
        print('Encoded String:\n')
        print(f'{ENCODED_STRING}\n')
        pyperclip.copy(ENCODED_STRING)
        print('Copied to clipboard\n')
        input('Press Enter: ')
        return

if __name__ == '__main__':
    while True:
        DICTIONARY = choose_encoding_type()
        ENCODED_STRING = encode_string(DICTIONARY)      