from courses.models import HomeworkSubmission
from .create_table_fpdf2 import PDF
import os
from django.core.files import File
def pdf_file_mark(request, file):
    homeworkSubmission = HomeworkSubmission.objects.filter(student = request.user.student.id)
    data = [
            ["Предмет", "Учитель", "Задача", "Оценка",],
    ]

    for info in homeworkSubmission:
            for count in range(1, 5):
                if count == 2:
                    data.append([info.homework.teacher.position, info.homework.teacher.user.first_name, info.homework.homework_title, str(info.submission_rating),])
    
    pdf = PDF()
    pdf.add_page()
    pdf.add_font("DejaVu", '', os.getenv("DEJA_VU"), uni=False,)
    pdf.set_font('DejaVu', size=10)
    pdf.create_table(table_data = data,title='Оценки за год', cell_width='even')
    pdf.ln()
    pdf.output('rating.pdf')

    f = open("rating.pdf", 'rb')
    myfile = File(f)
    file.file_ratings.save('rating.pdf', myfile)
