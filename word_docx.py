from docx import Document
from docx.enum.style import WD_STYLE_TYPE

doc = Document()
all_styles = doc.styles
table_styles = [s for s in all_styles if s.type == WD_STYLE_TYPE.TABLE]
for style in table_styles:
   print(style)