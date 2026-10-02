class Course:

  def __init__(self, course_id, name, credits):
    self.id = course_id
    self.name = name
    self.credits = credits

  def __str__(self):
    return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"