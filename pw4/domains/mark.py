import math
import numpy as np


def floor_to_one_decimal(val):
  return math.floor(val * 10) / 10.0


class MarkManager:

  def __init__(self):
    self.marks = {}  

  def add_mark(self, course_id, student_id, score):
    self.marks[(course_id, student_id)] = floor_to_one_decimal(score)

  def get_mark(self, course_id, student_id):
    return self.marks.get((course_id, student_id), None)

  def calculate_gpa(self, student_id, courses):
    student_marks = []
    student_credits = []

    for course in courses:
      score = self.get_mark(course.id, student_id)
      if score is not None:
        student_marks.append(score)
        student_credits.append(course.credits)

    if not student_credits:
      return 0.0

    np_marks = np.array(student_marks)
    np_credits = np.array(student_credits)

    return np.average(np_marks, weights=np_credits)