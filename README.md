# md2nw

Generate a novelWriter project from a work in progress written with any text editor or Markdown word processor.  

## Features

- Converts three levels of the novel structure: Parts, chapters, and scenes.

## Requirements

- [Python](https://www.python.org/) version 3.6+.

## Download link

[https://raw.githubusercontent.com/peter88213/md2nw/main/md2nw.py](https://raw.githubusercontent.com/peter88213/md2nw/main/md2nw.py)


## Instructions for use

### Command line usage

You can either

- launch the program on the command line passing the *.md* file as an argument, or
- launch the program via a batch file.

usage: `md2nw.py [-h] [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the *.md* file. 

#### optional arguments:

`-h, --help` 

show this help message and exit

`--silent` 

suppress error messages and the request to confirm overwriting

---

## Markdown reference


### Paragraphs

Double line breaks are considered paragraph breaks, as is the Markdown standard
supported by *novelWriter*. 

### Headings

#### Level 1 heading used for parts
`# One hash character at the start of the .`

#### Level 2 heading used for chapters
`## Two hash characters at the start of the line.`

#### Level 3 heading used as scene dividers  (not needed for the first scene in a  chapter).
`### Three hash characters at the start of the line.` Text, if any, is considered as the scene title. 

**NOTE:** On all levels, you can add an one-line synopsis to the heading, divided by `|`. 

### Emphasis

#### Italic 
`_single underscores_`

**Note** : A `_` surrounded with spaces will be treated as a literal underscore.

#### Bold 
`**double asterisks**`

#### Strikethrough 
`~~double swung dashes~~`

---

## Credits

- Frederik Lundh published the [xml pretty print algorithm](http://effbot.org/zone/element-lib.htm#prettyprint).

## License

md2nw is distributed under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

---

## See also


### nw_metadata

Create a cross reference table with novelWriter metadata. 

[nw_metadata](https://github.com/peter88213/nw_metadata)


### mm2nw

Generate a novelWriter project from a FreeMind/Freeplane outline.

[mm2nw](https://github.com/peter88213/mm2nw/)


### odt2nw

Generate a novelWriter project from a work in progress written with e.g. LibreOffice.

[odt2nw](https://github.com/peter88213/odt2nw/)


### yw2nw

Converter between yWriter and novelWriter.

[![yw2nw](img/yw2nw.png)](https://peter88213.github.io/yw2nw/)



