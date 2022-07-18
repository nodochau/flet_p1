
from cProfile import label
import flet
from flet import Checkbox, FloatingActionButton, Page, TextField, icons, Column, Row

def main(page: Page):
    new_task = TextField(hint_text="Whats needs to be done?", expand=True)
    task_view = Column()
    def add_clicked(e):
        # page.add(Checkbox(label=new_task.value))
        # new_task.value = ""
        # page.update()
      task_view.controls.append(Checkbox(label=new_task.value))
      new_task.value=''
      view.update()

    view = Column(
      width=600,
      controls=[
        Row(
          controls=[
            new_task,
            FloatingActionButton(icon=icons.ADD, on_click=add_clicked)
          ],
        ),
        task_view,
      ],
    )
    # page.add(new_task, FloatingActionButton(icon=icons.ADD, on_click=add_clicked))
    page.horizontal_alignment = 'center'
    page.add(view)

flet.app(target=main)