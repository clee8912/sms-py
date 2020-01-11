import Models
import csv

class StudentDAO:
    
    def __init__(self):
        self.s_list = []
        self.get_students()
    
    def get_students(self):
        try:
            with open('students.csv',mode = 'r+') as fo:
                for line in fo.read().split('\n'):
                    s_email, s_name, s_pw = line.split(',')
                    self.s_list.append(Models.Student(s_email,s_name,s_pw))

        except Exception:
            pass
            
        finally:
            return self.s_list
        
    def validate_user(self, email, pw):
        for Student in self.s_list:
            if Student.get_email() == email and Student.get_password() == pw:
                return True
        return False
    
    def get_student_by_email(self, email):
        for Student in self.s_list:

            if Student.get_email() == email:
                return Student
        return None
    
    def new_student(self, s_name, s_email, s_pw):
        s_em = [s_name, s_email]
        st_list = [[Student.course_id, Student.student_email] for Student in self.s_list]
        
        
        if s_em not in r_list:
            self.s_list.append(Models.Students(s_email, s_name, s_pw))
            self.save_student()      
            print(f'Student Added Successfully!')
            return True
        
        elif s_em in r_list:
            print(f'Student is already registered')
            return False

        else:
            print(f'Student is already registered')
            return False
                
    def save_student(self):
        try:
            with open('students.csv',mode = 'w') as fo:
                fo_writer = csv.writer(fo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for Student in self.s_list:
                    fo_writer.writerow([Student.get_email(),Student.get_name(),Student.s_password()])
                                        
        except Exception:
            pass
        
        finally:
            fo.close()
    

    
class CourseDAO:

    def __init__(self):
        self.c_list = []
        
    def get_courses(self):
        try:
            with open('courses.csv',mode = 'r+') as fo:
                for line in fo.read().split('\n'):
                    c_id, c_name, c_ins = line.split(',')
                    self.c_list.append(Models.Course(c_id,c_name,c_ins))
    
        except Exception:
            pass

            
        finally:
            fo.close()
            return self.c_list

    
class AttendingDAO:
    def __init__(self):
        self.a_list = []
        self.get_attending()
        
    def get_attending(self):
        try:
            with open('attending.csv',mode = 'r+') as fo:
                for line in fo.read().split('\n'):
                    c_id, s_email = line.split(',')
                    self.a_list.append(Models.Attending(c_id, s_email))
                                        
        except Exception:
            pass

            
        finally:
            fo.close()
            return self.a_list

    
    def get_student_courses(self, course_list, email):
        self.n_list = []
        
        for Course in course_list:
            for Attending in self.a_list:
                if (Attending.get_student_email() == email) and (Course.get_id() == Attending.get_course_id()):
                    self.n_list.append(Course)

        return self.n_list
    
    def register_student_to_course(self, email, course_id, course_list):

        c_list = [Course.get_id() for Course in course_list]
        r_em = [course_id, email]
        r_list = [[Attending.course_id, Attending.student_email] for Attending in self.a_list]
        
        if course_id not in c_list:
            print(f'Course not found')
            return False
        
        if r_em not in r_list:
            self.a_list.append(Models.Attending(course_id, email))
            self.save_attending()      
            print(f'Registration Successful!')
            return True
        
        elif r_em in r_list:
            print(f'You Are Already Registered In The Course.')
            return False

        else:
            print(f'Course not found')
            return False


    def save_attending(self):
        try:
            with open('attending.csv',mode = 'w') as fo:
                fo_writer = csv.writer(fo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator ='\n')
                for Attending in self.a_list:
                    fo_writer.writerow([Attending.get_course_id(),Attending.get_student_email()])
                                        
        except Exception:
            pass
        
        finally:
            fo.close()
            return True
