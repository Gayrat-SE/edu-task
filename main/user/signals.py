import csv
import os
import io

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Student, StudentBulkUpload, User


@receiver(post_save, sender=StudentBulkUpload)
def create_student_with_csv(sender, created, instance, *args, **kwargs):
    if created:
        opened = io.StringIO(instance.csv_file.read().decode('latin-1'))
        reading = csv.DictReader(opened, delimiter=",")
        students = []

        for row in reading:
            if "username" in row and row["username"]:
                username = row["username"]
                print(username)
                first_name = row["first_name"] if "first_name" in row and row["first_name"] else ""
                last_name = row["last_name"] if "last_name" in row and row["last_name"] else ""
                father_name = row["father_name"] if "father_name" in row and row["father_name"] else ""
                email = row["email"] if "email" in row and row["email"] else ""
                birthday = row["birthday ( YYYY-MM-DD )"] if "birthday ( YYYY-MM-DD )" in row and row["birthday ( YYYY-MM-DD )"] else ""
                phone = row["phone"] if "phone" in row and row["phone"] else ""
                gender = (
                    (row["gender"]).capitalize() if "gender" in row and row["gender"] else ""
                )

                check = User.objects.filter(username=username).exists()

                if not check:
                    password="1234"
                    users=User.objects.create(
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            father_name=father_name,
                            email=email,
                            phone="+"+phone,
                            gender=gender,
                            password=password
                    )
                    users.set_password(password)
                    users.save()
                    students.append(
                        Student(user=users)
                    )
        Student.objects.bulk_create(students)
        instance.csv_file.close()
        instance.save()




def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=StudentBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
    if instance.csv_file:
        _delete_file(instance.csv_file.path)