#! /usr/local/bin/python

"""
Extract code from a literate programming document in "noweb" format.
Originally developed by Jonathan Aquino (jonathan.aquino@gmail.com) and forked by Anormalien.
"""

import re
import sys

FILENAME = sys.argv[-1]
OUTPUT_CHUNK_NAME = sys.argv[-2][2:]
CHUNKS = {}

OPEN = '<<'
CLOSE = '>>'

with open(FILENAME) as file:
    for line in file:
        match = re.match(OPEN + '([^>]+)' + CLOSE + '=', line)
        if match:
            chunk_name = match.group(1)
            if not chunk_name in chunks:
                CHUNKS[chunk_name] = []
        else:
            match = re.match('@', line)
            if match:
                chunk_name = None
            elif chunk_name:
                CHUNKS[chunk_name].append(line)

                
def expand(chunk_name, indent):
    """
    Expand a chunk given its name and an indent.
    """
    expanded_chunk_lines = []
    for line in CHUNKS[chunk_name]:
        match = re.match('(\s*)' + OPEN + '([^>]+)' + CLOSE + '\s*$', line)
        if match:
            expanded_chunk_lines.extend(expand(match.group(2), indent + match.group(1)))
        else:
            expanded_chunk_lines.append(indent + line)
    return expanded_chunk_lines


for line in expand(OUTPUT_CHUNK_NAME, ''):
    print(line)
