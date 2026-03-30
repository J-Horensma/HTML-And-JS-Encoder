import sys, time, signal, base64, click, pyperclip
from Encoding_Libraries.HTML_entity_names import *
from Encoding_Libraries.HTML_decimal_entities import *
from Encoding_Libraries.HTML_hex_entities import *
from Encoding_Libraries.unicode_escape import *
from Encoding_Libraries.unicode_code_point_escape import *
from Encoding_Libraries.hex_escape import *
from Encoding_Libraries.octal_escape import *
from Encoding_Libraries.URL_encoding import *

def exit(signum, frame):
    click.clear()
    print('Exiting...')
    time.sleep(1)
    sys.exit(1)

def choose_encoding_type():
    while True:
        click.clear()
        print('HTML And JS Encoder')
        print('-------------------\n')
        ENCODING_OPTIONS = ['HTML Entity Names', 'Decimal HTML Entities', 'Hex HTML Entites', 'Unicode Escape', 'Unicode Code-Point Escape', 'Hex Escape','Octal Escape', 'base64 encoding', 'URL encoding']
        ENCODING_OPTIONS_INDEX = 1
        for VALUE in ENCODING_OPTIONS:
            print(f'{ENCODING_OPTIONS_INDEX}.) {VALUE}')
            ENCODING_OPTIONS_INDEX += 1
        ENCODING_CHOICE = input(f'\nChoose an encoding type (1-{(ENCODING_OPTIONS_INDEX - 1)}): ')

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
           INPUT = multi_line_input()
           INPUT_BYTES = INPUT.encode('utf-8')
           BASE64_BYTES = base64.b64encode(INPUT_BYTES)
           BASE64_ENCODED_STRING = BASE64_BYTES.decode('utf-8')
           click.clear()
           print('Encoded String:\n')
           print(BASE64_ENCODED_STRING,'\n')
           pyperclip.copy(ENCODED_STRING)
           print('Copied to clipboard\n')
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

def multi_line_input():
    while True:
        click.clear()
        signal.signal(signal.SIGBREAK, close_sys_stdin)
        print('1.) Type or paste a script, below')
        print('2.) Press "Enter", to ensure the last line registers')
        print('3.) Press "ctrl" + "break" to continue):\n')
        LINES = ''.join(sys.stdin.read()).strip()
        if LINES.strip():
            break
        else:
            print('Input, cannot be empty')
            input('Press Enter: ')
            continue
    return LINES

def get_string_list_line_offsets(LINE, STRING_LIST):
    LINE = LINE.strip()
    if LINE and STRING_LIST:
        if isinstance(LINE, str) and isinstance(STRING_LIST, list):
            STRING_LIST_OFFSETS = []
            for STRING in STRING_LIST:
                if STRING in LINE:

                    #LOOP AS MANY TIMES, AS THERE ARE MATCHED STRINGS, IN THE LINE VARIABLE,
                    #FOR THE CURRENT STRING ITERATION, OF THE "STRING_LIST" LIST
                    STRING_COUNT = LINE.count(STRING)
                    for COUNT_INDEX in range(STRING_COUNT):
                        if COUNT_INDEX > 0:
                            STRING_START = LINE.find(STRING, STRING_START + len(STRING))
                        else:
                            STRING_START = LINE.find(STRING)
                        if len(STRING) > 1:
                            STRING_END = (STRING_START + len(STRING) - 1)
                        else:
                            STRING_END = STRING_START

                        #ITERATE EACH CHARACTER, IN THE "LINE" VARIABLE, AND ADD EACH 
                        #CHARACTER OFFSET, MATCHING THE CURRENTLY ITERATED STRING OFFSET RANGE, TO A LIST,
                        #THAT WILL BE RETURNED
                        for CHARACTER_INDEX, CHARACTER in enumerate(LINE):
                            if CHARACTER_INDEX in range(STRING_START, (STRING_END + 1)):
                                STRING_LIST_OFFSETS.append(CHARACTER_INDEX)
            return STRING_LIST_OFFSETS
        else:
            raise TypeError('get_string_list_line_offsets():\nOne or more incorrect variable types, were supplied')
    else:
        raise EOFError('get_string_list_line_offsets():\nOne or more empty variables, were supplied')
        
def encode_string(DICTIONARY):
        INPUT = list(multi_line_input().split('\n'))
        click.clear()
        EXCLUDED_STRINGS = list(str(input('Enter a list of characters/continuous strings, separated by spaces, to leave unencoded (If any): ')).split())
        ENCODED_STRING = ''
        for LINE_INDEX, LINE in enumerate(INPUT):
            if EXCLUDED_STRINGS:
                STRING_LIST_LINE_OFFSETS = get_string_list_line_offsets(LINE, EXCLUDED_STRINGS)
            else:
                STRING_LIST_LINE_OFFSETS = list()
            for CHARACTER_INDEX, CHARACTER in enumerate(LINE):
                if CHARACTER in DICTIONARY and CHARACTER_INDEX not in STRING_LIST_LINE_OFFSETS:
                    ENCODED_CHARACTER = DICTIONARY[CHARACTER]
                    ENCODED_STRING = ENCODED_STRING + ENCODED_CHARACTER
                else:
                    ENCODED_STRING = ENCODED_STRING + CHARACTER    
        return ENCODED_STRING

if __name__ == '__main__':
    while True:
        try:
            signal.signal(signal.SIGINT, exit)
            DICTIONARY = choose_encoding_type()
            ENCODED_STRING = encode_string(DICTIONARY)
            click.clear()
            print('Encoded String:', '\n')
            print(ENCODED_STRING, '\n')
            pyperclip.copy(ENCODED_STRING)
            print('Copied to clipboard\n')
            input('Press Enter: ')
        except Exception as ERROR:
            print(ERROR)
            input('Press Enter: ')
