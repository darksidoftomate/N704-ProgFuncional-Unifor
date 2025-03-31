import unittest
from unittest.mock import MagicMock
from todo import ToDo  # Importe sua aplicação
import os

class TestToDo(unittest.TestCase):

    def setUp(self):
        """Configuração inicial: cria um banco de dados temporário e limpa a tabela."""
        self.test_db = "test_database.db"
        
        # Criar um mock para a página, para evitar o uso real do Flet
        mock_page = MagicMock()
        self.todo = ToDo(page=mock_page, db_name=self.test_db)  # Passa o banco de dados de teste
        self.todo.db_execute("DELETE FROM tasks")  # Limpa a tabela de tarefas antes de iniciar o teste

    def tearDown(self):
        """Limpa os testes após execução, removendo o banco de dados de teste."""
        # Fecha a conexão ao banco de dados antes de excluir o arquivo
        try:
            # Fechar a conexão com o banco de dados
            self.todo.db_execute("VACUUM")  # Realiza uma operação que força o fechamento da conexão
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

        # Exclui o banco de dados de teste
        if os.path.exists(self.test_db):
            os.remove(self.test_db)  # Exclui o banco de dados de teste após o teste
        else:
            print(f"{self.test_db} não encontrado.")  # Caso o arquivo não tenha sido criado por algum motivo

    def test_task_lifecycle(self):
        """Testa o ciclo completo: adicionar, marcar como concluída e excluir uma tarefa."""
        print("Passo 1: Adicionando tarefa")
        self.todo.db_execute("INSERT INTO tasks (name, status) VALUES (?, ?)", ["Teste", "incomplete"])
        result = self.todo.db_execute("SELECT * FROM tasks WHERE name = ?", ["Teste"])

        if result:
            print("Tarefa adicionada corretamente")
        else:
            print("Tarefa não encontrada")

        print("Passo 2: Marcando tarefa como concluída")
        self.todo.db_execute("UPDATE tasks SET status = ? WHERE name = ?", ["complete", "Teste"])
        result = self.todo.db_execute("SELECT status FROM tasks WHERE name = ?", ["Teste"])

        if result and result[0][0] == "complete":
            print("Tarefa marcada como concluída: complete")
        else:
            print("Erro ao marcar a tarefa como concluída")

        print("Passo 3: Excluindo tarefa")
        self.todo.db_execute("DELETE FROM tasks WHERE name = ?", ["Teste"])
        result = self.todo.db_execute("SELECT * FROM tasks WHERE name = ?", ["Teste"])

        if not result:
            print("Tarefa excluída com sucesso")
        else:
            print("Erro ao tentar excluir a tarefa")

if __name__ == '__main__':
    unittest.main(exit=False)
