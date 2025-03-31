import flet as ft
import sqlite3

class ToDo:
    def __init__(self, page: ft.Page, db_name="database.db"):
        self.page = page
        self.page.on_window_event = lambda e: self.fix_window_size(e)
        self.page.bgcolor = ft.Colors.WHITE
        self.page.window_maximized = False
        self.page.window_width = 100
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = "Tarefas diárias"
        self.task = ''
        self.view = 'all'

        # Closure para manipulação de banco de dados
        self.db_execute = self.create_db_manager(db_name)
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name TEXT, status TEXT)')
        self.results = self.db_execute('SELECT * FROM tasks')

        self.main_page()
        self.page.update()

    def fix_window_size(self, e):
        """Mantém o tamanho fixo da janela"""
        if e.data == "resized":
            self.page.window_width, self.page.window_height = 350, 450
            self.page.update()

    def create_db_manager(self, db_name):
        """Closure que retorna uma função para executar comandos SQL"""
        def execute(query, params=[]):
            # Usando o contexto with para garantir que a conexão seja fechada após cada operação
            with sqlite3.connect(db_name) as con:
                cur = con.cursor()
                cur.execute(query, params)
                con.commit()
                return cur.fetchall()
        return execute  # Retorna a função interna

    def update_task_list(self):
        """Atualiza a interface gráfica com a nova lista de tarefas"""
        if self.page:
            self.page.controls.pop()
            self.page.add(self.tasks_container())
            self.page.update()

    def checked(self, e):
        """Marca/desmarca uma tarefa e atualiza o status no banco de dados"""
        label, is_checked = e.control.label, e.control.value
        self.db_execute('UPDATE tasks SET status = ? WHERE name = ?', ["complete" if is_checked else "incomplete", label])
        self.results = self.db_execute('SELECT * FROM tasks' if self.view == 'all' else 'SELECT * FROM tasks WHERE status = ?', [self.view] if self.view != 'all' else [])
        self.update_task_list()

    def tasks_container(self):
        """Cria os componentes visuais das tarefas usando list comprehension"""
        return ft.Container(
            height=self.page.height * 0.8,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[
                        ft.Checkbox(
                            label=res[0], 
                            on_change=self.checked,
                            value=res[1] == 'complete'
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            icon_color=ft.Colors.RED,
                            data=res[0],
                            on_click=lambda e: self.delete_task(e.control.data)
                        )
                    ])
                    for res in self.results  # List Comprehension aplicada
                ]
            )
        )

    def set_value(self, e):
        """Armazena a tarefa digitada"""
        self.task = e.control.value

    def execute_task_operation(self, operation):
        """Função de alta ordem para operações de tarefa"""
        operation()
        self.results = self.db_execute('SELECT * FROM tasks')
        self.update_task_list()

    def add(self, e, input_task):
        """Adiciona uma nova tarefa"""
        if self.task:
            self.execute_task_operation(lambda: self.db_execute('INSERT INTO tasks VALUES (?, ?)', [self.task, 'incomplete']))
            input_task.value = ''
        self.page.update() if self.page else None

    def delete_task(self, task_name):
        """Remove uma tarefa do banco de dados"""
        self.execute_task_operation(lambda: self.db_execute("DELETE FROM tasks WHERE name = ?", [task_name]))

    def tabs_changed(self, e):
        """Atualiza a visualização das tarefas"""
        filtros = ["all", "incomplete", "complete"]
        self.view = filtros[e.control.selected_index]
        self.results = self.db_execute('SELECT * FROM tasks' if self.view == 'all' else 'SELECT * FROM tasks WHERE status = ?', [self.view] if self.view != 'all' else [])
        self.update_task_list()

    def main_page(self):
        """Configura a interface principal do aplicativo"""
        input_task = ft.TextField(
            hint_text='Digite uma tarefa:', color="black", expand=True, on_change=self.set_value
        )

        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: self.add(e, input_task))  #Lambda aplicada
            ]
        )

        tabs = ft.Tabs(
            selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text='Todos'), ft.Tab(text='Em andamento'), ft.Tab(text='Finalizados')]
        )

        if self.page:
            self.page.add(input_bar, tabs, self.tasks_container())

if __name__ == "__main__":
    ft.app(target=ToDo)
