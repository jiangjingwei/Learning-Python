import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

USERS_PATH = BASE_DIR + '/db/users'
SCHOOL_INFO = BASE_DIR + '/db/school_info'
COURSE_INFO = BASE_DIR + '/db/course_info'
TEACHER_INFO = BASE_DIR + '/db/teacher_info'
STUDENT_INFO = BASE_DIR + '/db/student_info'
CLASSES_INFO = BASE_DIR + '/db/classes_info'

ROLE = {
    '1': 'admin_sys',
    '2': 'teacher_sys',
    '3': 'student_sys',
}