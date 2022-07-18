import flet
from flet import Tab,Tabs, UserControl, TextField, Column, Row, FloatingActionButton, icons, page, Page

class TodoApp(UserControl):
  def build(self):
    # self.tasks = []
    self.new_task = TextField(hint_text='Whats needs to be done', expand=True)
    self.tasks = Column()

    self.filter = Tabs(
      selected_index=0,
      on_change=self.tabs_changed,
      tabs=[Tab(text='All'), Tab(text='Active'), Tab(text='Completed')]
    )
    self.view = Column(
      width=600,
      controls=[
        Row(
          controls=[
            self.new_task,
            FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
          ],
        ),
      ],
    )
    return Column(
          spacing=25,
          controls=[
            self.view, self.filter
          ],
        )
    

  def add_clicked(self, e):
    print("Button is clicked")

  def tabs_changed(self, e):
    print('Tab is pressed')

def main(page: Page):
  page.title = 'Tabs Demo'
  page.horizontal_alignment = 'center'
  page.update()
  app = TodoApp()
  page.add(app)

flet.app(target=main)