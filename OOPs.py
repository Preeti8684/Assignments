#!/usr/bin/env python
# coding: utf-8

# In[26]:


class Student:
    college_name="TIT&S"   #class attribute

    def _init_(self,name,age,dob):
        print("constructor has been called")
        self._name=name
        self._age=age
        self._dob=dob
    def print_name(self):
        print("student name: "+self._name)

        student=student("raj",23,"09/05/1994")
        print(student._name,student._age,student._dob)

#student_1.print_name()


# In[27]:


class Student:
    college_name="TIT&S"
    def print_name(self,name):
        print("student name:"+name)
        student=student()
print(student.college_name)
student.print_name("raj")
    


# In[ ]:




