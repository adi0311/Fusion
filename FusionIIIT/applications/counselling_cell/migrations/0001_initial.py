# Generated by Django 3.1.5 on 2021-04-22 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0003_auto_20191024_1242'),
        ('academic_information', '0005_auto_20200522_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounsellingIssueCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CounsellingMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_time', models.DateTimeField()),
                ('agenda', models.TextField()),
                ('venue', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyCounsellingTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_position', models.CharField(choices=[('head_counsellor', 'Head Counsellor'), ('faculty_counsellor', 'Faculty Counsellor')], max_length=50)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.faculty')),
            ],
            options={
                'unique_together': {('faculty', 'faculty_position')},
            },
        ),
        migrations.CreateModel(
            name='StudentCounsellingTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_position', models.CharField(choices=[('student_guide', 'Student Guide'), ('student_coordinator', 'Student Coordinator')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('student_id', 'student_position')},
            },
        ),
        migrations.CreateModel(
            name='StudentMeetingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_time', models.DateTimeField()),
                ('description', models.TextField(max_length=1000)),
                ('requested_meeting_status', models.CharField(choices=[('status_accepted', 'Accepted'), ('status_pending', 'Pending')], default='status_pending', max_length=20)),
                ('recipient_reply', models.TextField(max_length=1000)),
                ('requested_faculty_invitie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.facultycounsellingteam')),
                ('requested_student_invitie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.studentcounsellingteam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCounsellingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_counsellor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.facultycounsellingteam')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
                ('student_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.studentcounsellingteam')),
            ],
        ),
        migrations.CreateModel(
            name='CounsellingMinutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counselling_minutes', models.FileField(upload_to='counselling_cell/')),
                ('counselling_meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.counsellingmeeting')),
            ],
        ),
        migrations.AddField(
            model_name='counsellingmeeting',
            name='faculty_invities',
            field=models.ManyToManyField(to='counselling_cell.FacultyCounsellingTeam'),
        ),
        migrations.AddField(
            model_name='counsellingmeeting',
            name='meeting_host',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='counsellingmeeting',
            name='student_invities',
            field=models.ManyToManyField(to='academic_information.Student'),
        ),
        migrations.CreateModel(
            name='CounsellingIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField(max_length=500)),
                ('issue_status', models.CharField(choices=[('status_unresolved', 'Unresolved'), ('status_resolved', 'Resolved'), ('status_inprogress', 'InProgress')], default='status_unresolved', max_length=20)),
                ('issue_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.counsellingissuecategory')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='CounsellingFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counselling_question', models.TextField(max_length=1000)),
                ('counselling_answer', models.TextField(max_length=5000)),
                ('counseliing_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling_cell.counsellingissuecategory')),
            ],
        ),
    ]
