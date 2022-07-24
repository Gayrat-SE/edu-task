from .create_table_fpdf2 import PDF
import os
from courses.models import HomeworkSubmission
from django.core.files import File
def pdf_file_mark(request, data):
    file =  HomeworkSubmission.objects.filter(student = request.user.student)[0]
    pdf = PDF()
    pdf.add_page()
    pdf.add_font("DejaVu", '', os.getenv("DEJA_VU"), uni=False,)
    pdf.set_font('DejaVu', size=10)
    pdf.create_table(table_data = data,title='I\'m the first title', cell_width='even')
    pdf.ln()
    # pdf.output('rating.pdf')

    # f = open("rating.pdf", 'rb')
    # myfile = File(f)
    # file.file_ratings.save('rating.pdf', myfile)
