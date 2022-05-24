from googletrans.constants import LANGUAGES

PREFIX = '!'

TRANS_COMMANDS = ['t'] + ['t-'+key for key in LANGUAGES.keys()]
GET_COMMANDS = ['g']
CODE_COMMANDS = ['c']