import re

TOKEN_REGEXES = [
    (r'//.*', 'COMMENT'),
    (r'/\*.*?\*/', 'COMMENT'),
    (r'\".*?\"', 'STRING_LITERAL'),
    (r'\'[^\']*\'', 'CHARACTER_LITERAL'),
    (r'\b(bool|char|double|float|int|long|short|void)\b', 'DATA_TYPE'),
    (r'\b(if|else|while|do|for|switch|case|break|continue|return)\b', 'KEYWORD'),
    (r'\b(true|false)\b', 'BOOLEAN_LITERAL'),
    (r'[a-zA-Z_]\w*', 'IDENTIFIER'),
    (r'[+-]?\d+\.\d+', 'FLOAT_LITERAL'),
    (r'[+-]?\d+', 'INTEGER_LITERAL'),
    (r'\+\+', 'INCREMENT'),
    (r'--', 'DECREMENT'),
    (r'==', 'EQUAL_TO'),
    (r'!=', 'NOT_EQUAL_TO'),
    (r'&&', 'LOGICAL_AND'),
    (r'\|\|', 'LOGICAL_OR'),
    (r'<=', 'LESS_THAN_OR_EQUAL_TO'),
    (r'>=', 'GREATER_THAN_OR_EQUAL_TO'),
    (r'[^\w\s]', 'PUNCTUATION'),
    (r'\s+', 'WHITESPACE'),
]


def lex(source_code):
    tokens = []
    pos = 0

    while pos < len(source_code):
        match = None
        for regex, token_type in TOKEN_REGEXES:
            pattern = re.compile(regex)
            match = pattern.match(source_code, pos)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE' and token_type != 'COMMENT':
                    tokens.append((value, token_type))
                pos = match.end(0)
                break

        if not match:
            raise Exception('Invalid token: %s' % source_code[pos])

    return tokens


source_code = '''
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}
'''
tokens = lex(source_code)
print(tokens)