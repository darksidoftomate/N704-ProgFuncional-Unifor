# N704 - Programação Funcional

# Grupo 38
    Adline Alves - 2313557 - Documentação e levantamento de requisitos
    Alano Dantas - 2222891 - Testes funcionais
    Levi Ribeiro - 2317790 - Desenvolvimento
    Matheus Pinheiro - 2314205 - Desenvolvimento

# Introdução
    Documento apresentando relatório e levantamento dos objetivos do projeto de Programação Funcional. O projeto consiste no desenvolvimento de um gerenciador de tarefas em Python, utilizando os conceitos abordados na disciplina. O gerenciador será desenvolvido com Python, Flet e SQLite, permitindo adicionar, visualizar, atualizar o status e excluir tarefas.

# Objetivo do Sistema
    O sistema deve permitir a criação, listagem, filtragem e remoção de tarefas, com foco na utilização dos conceitos de programação funcional definidos na proposta da atividade.

# Requisitos

    1. Requisitos Funcionais

        1.1 - Requisitos de Cadastro e Gerenciamento de Tarefas

            - O sistema deve permitir a criação de novas tarefas.
            - O sistema deve permitir que o usuário visualize todas as tarefas cadastradas.
            - O sistema deve permitir que o usuário filtre tarefas entre todas, em andamento e concluídas.
            - O sistema deve permitir que o usuário marque tarefas como concluídas.
            - O sistema deve permitir a exclusão de tarefas.

        1.2 - Requisitos de Interface

            -O sistema deve possuir uma interface gráfica responsiva baseada no Flet.
            - A interface deve conter um campo de entrada para adição de tarefas e um botão de confirmação.
            - As tarefas devem ser listadas em forma de checkbox, permitindo marcação/desmarcação.
            - O sistema deve exibir um botão de exclusão ao lado de cada tarefa cadastrada.
            - O sistema deve ter uma barra de abas com opções de filtragem: Todos, Em andamento, Finalizados.

        1.3 - Requisitos de Banco de Dados

            - O sistema deve armazenar tarefas em um banco de dados SQLite.
            - O banco de dados deve conter uma tabela chamada tasks com as colunas:
                - name - Nome da tarefa.
                - status - Estado da tarefa ("incomplete" ou "complete").
            - O sistema deve permitir a recuperação e manipulação de dados do banco usando funções de alta ordem e closures.

        2. Requisitos Não Funcionais

            2.1 - O sistema deve ser implementado em Python.
            2.2 - A interface do usuário deve ser desenvolvida utilizando Flet.
            2.3 - O banco de dados utilizado deve ser SQLite.
            2.4 - O sistema deve ser leve e de fácil instalação, sem dependências externas complexas.

# Conceitos Utilizados
O código usará dos seguintes conceitos de programação funcional:

    • Função Lambda → Para filtragem de tarefas.
    • List Comprehension → Para manipulação e exibição das tarefas.
    • Closure → Para armazenar as tarefas de forma encapsulada.
    • Função de Alta Ordem → Para aplicar operações genéricas sobre as tarefas.

# Uso de Ferramentas de Apoio
    Durante o desenvolvimento do projeto, utilizamos o ChatGPT como ferramenta complementar para revisão e refinamento da documentação. 
    O modelo foi empregado para estruturar descrições, garantir a clareza dos requisitos e validar a aderência do código aos conceitos de programação funcional exigidos pela disciplina.
    Todas as decisões de implementação e desenvolvimento do código foram realizadas pela equipe, 
    utilizando o ChatGPT exclusivamente como suporte na organização das informações e na verificação da coerência dos conteúdos apresentados.
