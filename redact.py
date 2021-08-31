import re
import sys
from datetime import datetime

import pdf_redactor

# Capture any redactor options.
options = pdf_redactor.RedactorOptions()

# Build our expression list using any provided words.
word = sys.argv[2]
words = word.split('|')
expressions = []

for word in words:
    expressions.append((
        re.compile(r"(" + word.strip() + ")"),
        lambda m : ""
    ))

# Perform the redaction using PDF on standard input and writing to standard output.
options.content_filters = expressions
pdf_redactor.redactor(options)
