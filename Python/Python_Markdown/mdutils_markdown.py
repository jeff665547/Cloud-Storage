import os
from pathlib import Path
import mdutils as md

path = Path(r"C:\Users\jeff\Desktop\Learning\Python\Python_Markdown")
os.chdir(path)

#%% Create a Markdown File with the Specified Filename and Title

file_name = "Title and File Name"

mdFile = md.MdUtils(file_name = file_name, title = "Title Example")
mdFile.create_md_file()

#%% Create the TOC (table of contents)
file_name = "TOC"

mdFile = md.MdUtils(file_name = file_name, title = "TOC Example")

mdFile.new_table_of_contents(table_title = "B Contents", depth = 2)

mdFile.create_md_file()

#%% Paragraph and Text Format
# new_paragraph method writes text in a markdown file with jumping an entirely empty new line.
# You can give format to text using the arguments bold_italics_code, color and align

file_name = "Paragraph and Text Format"

mdFile = md.MdUtils(file_name = file_name, title = "Paragraph and Text Format Example")

mdFile.new_paragraph("This is a sentence.")
mdFile.new_paragraph("This is a paragraph: new_paragraph method let you can very easily add a new paragraph."
                     "This example of paragraph has been added using this method. Moreover,"
                     "new_paragraph method make your live easy because it can give format"
                     " to the text. Lets see an example:")
mdFile.new_paragraph("This is a ``code`` in a sentence.")
mdFile.new_paragraph("This is an example of text in which has been bold text.")
mdFile.new_paragraph("This is an example of text in which has been italics text.")
mdFile.new_paragraph("This is an example of code in which entire text are code formatted, "
                     "bold, and italical", 
                     bold_italics_code='bic')
mdFile.new_paragraph("This is an example of text in which has been added color (purple), "
                     "bold and italics text.", 
                     bold_italics_code='bi', color = "purple")

mdFile.create_md_file()

#%% New Line Break
# new_line method writes text in a markdown file without jumping an entirely 
# empty new line. As new_paragraph, you can give format to text using the arguments
# bold_italics_code, color and align

file_name = "New Line"

mdFile = md.MdUtils(file_name = file_name, title = "New Line Example")

mdFile.new_line("This is an example of line break which has been created with ``new_line`` method.")
mdFile.new_line("This is an inline code which contains bold and italics text and it is centered", 
                bold_italics_code='cib', align='center')

mdFile.create_md_file()

#%% Keep Writing without a "\n".
# new_line method writes text in a markdown file without using "\n", and as 
# new_paragraph and new_line, you can give format to text using the arguments
# bold_italics_code, color and align

file_name = "Write"

mdFile = md.MdUtils(file_name = file_name, title = "Write Example")

mdFile.write("The following text has been written with ``write`` method."
             " You can use markdown directives to write:"
             "**bold**, _italics_, ``inline_code``... or ")
mdFile.write("use the following available parameters:  \n")
mdFile.write('  \n')
mdFile.write('bold_italics_code', bold_italics_code='bic')
mdFile.write('  \n')
mdFile.write('Text color', color='green')
mdFile.write('  \n')
mdFile.write('Align Text to center', align='center')

mdFile.create_md_file()

#%% Create a Table
file_name = "Create a table"

mdFile = md.MdUtils(file_name = file_name, title = "Create a Table Exmaple")

list_of_strings = ["Items", "Descriptions", "Data"]
for x in range(5):
    list_of_strings.extend(["Item " + str(x), "Description Item " + str(x), str(x)])
mdFile.new_line()
mdFile.new_table(columns=3, rows=6, text=list_of_strings, text_align='center')

mdFile.create_md_file()