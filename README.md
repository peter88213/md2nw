# md2nw

Generate a novelWriter project from a work in progress written with any text editor or Markdown word processor.  

## Features

- Converts three levels of the novel structure: Parts, chapters, and scenes.

## Requirements

- [Python](https://www.python.org/) version 3.6+.

## Download link

[https://raw.githubusercontent.com/peter88213/md2nw/main/md2nw.py](https://raw.githubusercontent.com/peter88213/md2nw/main/md2nw.py)


## Instructions for use

### Intended usage

After placing the downloaded script **md2nw.py** to a convenient place, you might want to create a shortcut on the desktop. 

If you drag a text document with extension *.md* and drop it on the icon, a new novelWriter project is generated in a directory named after the document. 

Existing novelWriter project directories will be renamed as a whole and get the extension *.bak*. 
If there is already such a directory, a new, numbered backup directory is created with the  extension *.bkxxxx*

### Command line usage

Alternatively, you can

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

#### Level 3 heading used as scene dividers  (not needed for the first scenes in a  chapter).
`### Three hash characters at the start of the line.` Text, if any, is considered as the scene title. 

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

