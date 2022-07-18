import flet
from flet import TextField, Column, Row, FloatingActionButton, Page, UserControl, icons, Checkbox

class ToDoApp(UserControl):
  def __init__(self, texttitle):
    self.textTitle = texttitle
    super().__init__()
  def build(self):
      
      self.new_task = TextField(hint_text=self.textTitle, expand=True)
      self.tasks = Column()

      return Column(
          width=600,
          controls=[
              Row(
                controls=[
                  self.new_task,
                  FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked)
                ],
              ),
              self.tasks,
          ],
      )
  def add_clicked(self, e):
    self.tasks.controls.append(Checkbox(label=self.new_task.value))
    self.new_task = ''
    self.update()

def main(page: Page):
  page.title = 'ToDo App'
  page.horizontal_alignment = 'center'
  page.update()

  app1 = ToDoApp(texttitle='What needs to be done')
  
  app2 = ToDoApp(texttitle='Tasks need to be finished')
  
  page.add(app1, app2)
flet.app(target=main)
