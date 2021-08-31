# PDF Scrubber

### Overview

This utility makes use of the `PDF Redactor` module to remove
a series of words from an input PDF. A basic usage example is
illustrated ahead.

**Usage:**

```
python3 redact.py < input.pdf > output.pdf -o "example 1 | example 2 | example 3 | etc"
```

**Options:**

`-o` One or more pipe delimited words or phrases to remove from the input PDF file.

### Credits

[PDF Redactor](https://github.com/JoshData/pdf-redactor)