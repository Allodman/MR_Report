import docx
from docx.shared import Mm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_LINE_SPACING
from datetime import datetime, date, time
import Google_docs

report_month = datetime.timetuple(datetime.now())[1] - 1
print(report_month)

doc = docx.Document()
# Стиль текста по умолчанию
style = doc.styles['Normal'] # Стиль для всего документа
style.font.name = 'TimesNewRomanPSMT' # Шрифт для всего документа
style.font.size = Pt(11) # Размер шрифта

# Добавление дотабличного текста
header = doc.add_paragraph('')
header.add_run('Акт сдачи-приемки оказанных услуг.').bold = True
header.alignment = WD_ALIGN_PARAGRAPH.CENTER

par1 = doc.add_paragraph('')
par1.add_run('Акционерное общество «МР Групп» ').bold = True
par1.add_run('(АО «МР Групп»), зарегистрированное и действующее в соответствии с законодательством '
             'Российской Федерации, именуемое в дальнейшем «Заказчик», в лице Исполнительного директора '
             'Обухова Александра Анатольевича, действующего на основании доверенности '
             'от 31.12.2021 No ИД-2022, с одной стороны, и ')
par1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
fmt = par1.paragraph_format
fmt.first_line_indent = Mm(12.7)

par2 = doc.add_paragraph('')
par2.add_run("Общество с ограниченной ответственностью «Мультиспейс Павелецкая» ").bold = True
par2.add_run('(ООО «Мультиспейс Павелецкая»), именуемое в дальнейшем «Исполнитель», '
             'в лице Генерального директора управляющей организации ООО «Прайдекс Констракшн» '
             'Бренева Кирилла Сергеевича, действующего на основании Устава и Договора No 1 передачи '
             'полномочий единоличного исполнительного органа ООО «Электросистемс» от 18.11.2019г., с '
             'другой стороны, далее совместно именуемые «Стороны», а по отдельности – «Сторона», '
             'составили настоящий акт (далее - Акт) о нижеследующем:')
par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
fmt2 = par2.paragraph_format
fmt2.first_line_indent = Mm(12.7)

par3 = doc.add_paragraph(f'1. Исполнителем были оказаны следующие услуги за период с 01.07.2022г. по 30.06.2022г. '
                         '(далее - Отчетный период) по Договору возмездного оказания услуг '
                         'No 41254 (далее - Договор): ')
par3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
fmt3 = par3.paragraph_format
fmt3.first_line_indent = Mm(12.7)

review = Google_docs.last_month_review

table = doc.add_table(len(review) + 1, 3) # (строка, колонка) | Создаём таблицу
table.style = 'Table Grid' # Стиль таблицы (Шоб рамки были видны)
cell = table.cell(0, 0).add_paragraph('')
cell.add_run("Дата")
cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
cell = table.cell(0, 1).add_paragraph('')
cell.add_run("Описание услуги/инцидента")
cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
cell = table.cell(0, 2).add_paragraph('')
cell.add_run("Актуальный статус")
cell.alignment = WD_ALIGN_PARAGRAPH.CENTER
for row in range(len(review)):
    for column in range(3):
        cell = table.cell(row + 1, column).add_paragraph('')
        cell.add_run(review[row][column])
        cell.alignment = WD_ALIGN_PARAGRAPH.CENTER




# Сохранение документа
doc.save(f'C:\\Users\\anton.kudryashov\\Documents\\Акт сдачи-приемки оказанных услуг (Тех поддержка) 0{report_month}.22.docx')
