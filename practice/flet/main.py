# # import flet as ft
# # import time
# # def main(page: ft.Page):
# #     t = ft.Text(value="Hello, world!", color="green")
# #     page.controls.append(t)
# #     page.update()

# #     # t = ft.Text()
# #     # page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

# #     # for i in range(10):
# #     #     t.value = f"Step {i}"
# #     #     page.update()
# #     #     time.sleep(1)

# # #     page.add(
# # #     ft.Row(controls=[
# # #         ft.Text("A"),
# # #         ft.Text("B"),
# # #         ft.Text("C")
# # #     ])
# # # )
# # #     page.add(
# # #     ft.Row(controls=[
# # #         ft.TextField(label="Your name"),
# # #         ft.ElevatedButton(text="Say my name!")
# # #     ])
# # # )
# #     # for i in range(10):
# #     #     page.controls.append(ft.Text(f"Line {i}"))
# #     #     if i > 4:
# #     #         page.controls.pop(0)
# #     #     page.update()
# #     #     time.sleep(0.3)
# #     def button_clicked(e):
# #         page.add(ft.Text("Clicked!"))

# #     page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
# # ft.app(main)
# # import flet as ft

# # def main(page):
# #     # def add_clicked(e):
# #     #     page.add(ft.Checkbox(label=new_task.value))
# #     #     new_task.value = ""
# #     #     new_task.focus()
# #     #     new_task.update()

# #     # new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
# #     # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
# #     # first_name = ft.TextField()
# #     # last_name = ft.TextField()
# #     # first_name.enabled = True
# #     # last_name.disabled = True
# #     # page.add(first_name, last_name)
# #     first_name = ft.TextField()
# #     last_name = ft.TextField()
# #     c = ft.Column(controls=[
# #         first_name,
# #         last_name
# #     ])
# #     c.disabled = True
# #     page.add(c)
# # ft.app(main)
# import flet as ft

# def main(page):
#     def btn_click(e):
#         if not txt_name.value:
#             txt_name.error_text = "Please enter your name"
#             page.update()
#         else:
#             name = txt_name.value
#             page.clean()
#             page.add(ft.Text(f"Hello, {name}!"))

#     txt_name = ft.TextField(label="Your name")

#     page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))

# ft.app(main)
import flet as ft
class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main(page: ft.Page):

    page.add(
        Task(text="Do laundry"),
        Task(text="Cook dinner"),
    )


ft.app(main)