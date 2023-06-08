"""Provide a base class for Markdown formatted text files.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/PyWriter
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
from pywriter.pywriter_globals import *
from pywriter.file.file import File
from pywriter.model.chapter import Chapter
from pywriter.model.scene import Scene
from pywriter.model.id_generator import create_id


class MdFile(File):
    """Markdown file representation.
    
    Public methods:
        read() -- Parse the file and get the instance variables.

    Provide methods and data for processing chapters with formatted text.
    """
    DESCRIPTION = _('Markdown File')
    EXTENSION = '.md'
    PART_SEPARATOR: str = '# '
    CHAPTER_SEPARATOR: str = '## '
    SCENE_SEPARATOR: str = '### '
    DESC_SEPARATOR: str = '|'
    LOW_WORDCOUNT = 10
    # Defines the difference between "Outline" and "Draft"

    def read(self):
        """Parse the file and get the instance variables.
        
        Return a message beginning with the ERROR constant in case of error.
        """

        def split_heading(line):
            heading = line.strip('# ').split(self.DESC_SEPARATOR)
            title = heading[0]
            try:
                desc = heading[1]
            except:
                desc = None
            return title, desc

        def write_scene_content(scId, lines):
            if scId is not None:
                text = '\n'.join(lines)
                self.novel.scenes[scId].sceneContent = text
                if self.novel.scenes[scId].wordCount < self.LOW_WORDCOUNT:
                    self.novel.scenes[scId].status = 1
                    # Outline
                else:
                    self.novel.scenes[scId].status = 2
                    # Draft

        chCount = 0
        scCount = 0
        lines = []
        chId = None
        scId = None
        try:
            with open(self.filePath, 'r', encoding='utf-8') as f:
                mdText = f.read()
                mdLines = (mdText).split('\n')
        except(FileNotFoundError):
            raise Error(f'{_("File not found")}: "{norm_path(self.filePath)}".')

        except:
            try:
                # the file may be ANSI encoded.
                with open(self.filePath, 'r') as f:
                    mdText = f.read()
            except:
                raise Error(f'{_("Cannot read file")}: "{norm_path(self.filePath)}".')

        for mdLine in mdLines:
            if mdLine.startswith('#'):
                title, desc = split_heading(mdLine)

                # Write previous scene.
                write_scene_content(scId, lines)
                scId = None
            if mdLine.startswith(self.PART_SEPARATOR) or mdLine.startswith(self.CHAPTER_SEPARATOR):

                # Add a chapter.
                chCount += 1
                chId = str(chCount)
                self.novel.chapters[chId] = Chapter()
                self.novel.chapters[chId].title = title
                self.novel.chapters[chId].desc = desc
                self.novel.chapters[chId].chType = 0
                self.novel.chapters[chId].srtScenes = []
                if mdLine.startswith(self.PART_SEPARATOR):
                    self.novel.chapters[chId].chLevel = 1
                else:
                    self.novel.chapters[chId].chLevel = 0
                self.novel.srtChapters.append(chId)
            elif scId is not None:
                lines.append(mdLine)
            elif mdLine and chId is not None:
                if mdLine.startswith(self.SCENE_SEPARATOR):
                    lines = []
                else:
                    lines = [mdLine]
                    title = None
                    desc = None
                # Add a scene; drop the first line if empty.
                scCount += 1
                scId = str(scCount)
                self.novel.scenes[scId] = Scene()
                self.novel.chapters[chId].srtScenes.append(scId)
                self.novel.scenes[scId].status = 1
                # Outline by default
                if not title:
                    title = f'Scene {scCount}'
                self.novel.scenes[scId].title = title
                self.novel.scenes[scId].desc = desc
