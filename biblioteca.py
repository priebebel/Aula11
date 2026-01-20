"""
Sistema de Biblioteca - Aula 11
Sistema simples de gerenciamento de biblioteca
"""

from datetime import datetime, timedelta


class Livro:
    """Classe que representa um livro na biblioteca"""
    
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.emprestado_para = None
        self.data_emprestimo = None
    
    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para}"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}, Ano: {self.ano_publicacao}) - {status}"


class Membro:
    """Classe que representa um membro da biblioteca"""
    
    def __init__(self, nome, id_membro, email):
        self.nome = nome
        self.id_membro = id_membro
        self.email = email
        self.livros_emprestados = []
    
    def __str__(self):
        qtd_livros = len(self.livros_emprestados)
        return f"{self.nome} (ID: {self.id_membro}, Email: {self.email}) - {qtd_livros} livro(s) emprestado(s)"


class Biblioteca:
    """Classe principal que gerencia a biblioteca"""
    
    def __init__(self, nome):
        self.nome = nome
        self.livros = {}  # isbn -> Livro
        self.membros = {}  # id_membro -> Membro
        self.dias_emprestimo = 14  # Prazo padrão de empréstimo
    
    # Métodos de gerenciamento de livros
    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca"""
        if livro.isbn in self.livros:
            print(f"Erro: Livro com ISBN {livro.isbn} já existe na biblioteca.")
            return False
        self.livros[livro.isbn] = livro
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")
        return True
    
    def remover_livro(self, isbn):
        """Remove um livro da biblioteca"""
        if isbn not in self.livros:
            print(f"Erro: Livro com ISBN {isbn} não encontrado.")
            return False
        livro = self.livros[isbn]
        if not livro.disponivel:
            print(f"Erro: Não é possível remover o livro '{livro.titulo}' pois está emprestado.")
            return False
        del self.livros[isbn]
        print(f"Livro '{livro.titulo}' removido com sucesso!")
        return True
    
    def listar_livros(self):
        """Lista todos os livros da biblioteca"""
        if not self.livros:
            print("Nenhum livro cadastrado na biblioteca.")
            return
        print(f"\n=== Livros da {self.nome} ===")
        for livro in self.livros.values():
            print(f"  - {livro}")
    
    def buscar_livro_por_titulo(self, titulo):
        """Busca livros por título"""
        resultados = [livro for livro in self.livros.values() 
                     if titulo.lower() in livro.titulo.lower()]
        if not resultados:
            print(f"Nenhum livro encontrado com o título '{titulo}'.")
            return []
        print(f"\nEncontrado(s) {len(resultados)} livro(s):")
        for livro in resultados:
            print(f"  - {livro}")
        return resultados
    
    def buscar_livro_por_autor(self, autor):
        """Busca livros por autor"""
        resultados = [livro for livro in self.livros.values() 
                     if autor.lower() in livro.autor.lower()]
        if not resultados:
            print(f"Nenhum livro encontrado do autor '{autor}'.")
            return []
        print(f"\nEncontrado(s) {len(resultados)} livro(s):")
        for livro in resultados:
            print(f"  - {livro}")
        return resultados
    
    # Métodos de gerenciamento de membros
    def adicionar_membro(self, membro):
        """Adiciona um membro à biblioteca"""
        if membro.id_membro in self.membros:
            print(f"Erro: Membro com ID {membro.id_membro} já existe.")
            return False
        self.membros[membro.id_membro] = membro
        print(f"Membro '{membro.nome}' cadastrado com sucesso!")
        return True
    
    def remover_membro(self, id_membro):
        """Remove um membro da biblioteca"""
        if id_membro not in self.membros:
            print(f"Erro: Membro com ID {id_membro} não encontrado.")
            return False
        membro = self.membros[id_membro]
        if membro.livros_emprestados:
            print(f"Erro: Não é possível remover o membro '{membro.nome}' pois possui livros emprestados.")
            return False
        del self.membros[id_membro]
        print(f"Membro '{membro.nome}' removido com sucesso!")
        return True
    
    def listar_membros(self):
        """Lista todos os membros da biblioteca"""
        if not self.membros:
            print("Nenhum membro cadastrado na biblioteca.")
            return
        print(f"\n=== Membros da {self.nome} ===")
        for membro in self.membros.values():
            print(f"  - {membro}")
    
    # Métodos de empréstimo
    def emprestar_livro(self, isbn, id_membro):
        """Empresta um livro para um membro"""
        if isbn not in self.livros:
            print(f"Erro: Livro com ISBN {isbn} não encontrado.")
            return False
        if id_membro not in self.membros:
            print(f"Erro: Membro com ID {id_membro} não encontrado.")
            return False
        
        livro = self.livros[isbn]
        membro = self.membros[id_membro]
        
        if not livro.disponivel:
            print(f"Erro: O livro '{livro.titulo}' não está disponível.")
            return False
        
        livro.disponivel = False
        livro.emprestado_para = membro.nome
        livro.data_emprestimo = datetime.now()
        membro.livros_emprestados.append(isbn)
        
        data_devolucao = livro.data_emprestimo + timedelta(days=self.dias_emprestimo)
        print(f"Livro '{livro.titulo}' emprestado para '{membro.nome}' com sucesso!")
        print(f"Data de devolução: {data_devolucao.strftime('%d/%m/%Y')}")
        return True
    
    def devolver_livro(self, isbn):
        """Registra a devolução de um livro"""
        if isbn not in self.livros:
            print(f"Erro: Livro com ISBN {isbn} não encontrado.")
            return False
        
        livro = self.livros[isbn]
        
        if livro.disponivel:
            print(f"Erro: O livro '{livro.titulo}' não está emprestado.")
            return False
        
        # Encontrar o membro que tem o livro
        membro = None
        for m in self.membros.values():
            if isbn in m.livros_emprestados:
                membro = m
                break
        
        if membro:
            membro.livros_emprestados.remove(isbn)
        
        print(f"Livro '{livro.titulo}' devolvido com sucesso!")
        livro.disponivel = True
        livro.emprestado_para = None
        livro.data_emprestimo = None
        return True
    
    def listar_livros_disponiveis(self):
        """Lista apenas os livros disponíveis"""
        disponiveis = [livro for livro in self.livros.values() if livro.disponivel]
        if not disponiveis:
            print("Nenhum livro disponível no momento.")
            return
        print(f"\n=== Livros Disponíveis na {self.nome} ===")
        for livro in disponiveis:
            print(f"  - {livro}")
    
    def listar_livros_emprestados(self):
        """Lista apenas os livros emprestados"""
        emprestados = [livro for livro in self.livros.values() if not livro.disponivel]
        if not emprestados:
            print("Nenhum livro emprestado no momento.")
            return
        print(f"\n=== Livros Emprestados ===")
        for livro in emprestados:
            data_devolucao = livro.data_emprestimo + timedelta(days=self.dias_emprestimo)
            print(f"  - {livro} - Devolução: {data_devolucao.strftime('%d/%m/%Y')}")


def menu_principal():
    """Interface de menu para o sistema de biblioteca"""
    biblioteca = Biblioteca("Biblioteca Aula 11")
    
    while True:
        print("\n" + "="*50)
        print(f"  {biblioteca.nome}")
        print("="*50)
        print("1. Gerenciar Livros")
        print("2. Gerenciar Membros")
        print("3. Empréstimos e Devoluções")
        print("4. Buscar Livros")
        print("5. Relatórios")
        print("0. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_livros(biblioteca)
        elif opcao == "2":
            menu_membros(biblioteca)
        elif opcao == "3":
            menu_emprestimos(biblioteca)
        elif opcao == "4":
            menu_buscar(biblioteca)
        elif opcao == "5":
            menu_relatorios(biblioteca)
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


def menu_livros(biblioteca):
    """Menu para gerenciamento de livros"""
    while True:
        print("\n--- Gerenciar Livros ---")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Listar Todos os Livros")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            isbn = input("ISBN: ").strip()
            ano = input("Ano de Publicação: ").strip()
            livro = Livro(titulo, autor, isbn, ano)
            biblioteca.adicionar_livro(livro)
        elif opcao == "2":
            isbn = input("ISBN do livro a remover: ").strip()
            biblioteca.remover_livro(isbn)
        elif opcao == "3":
            biblioteca.listar_livros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_membros(biblioteca):
    """Menu para gerenciamento de membros"""
    while True:
        print("\n--- Gerenciar Membros ---")
        print("1. Adicionar Membro")
        print("2. Remover Membro")
        print("3. Listar Todos os Membros")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Nome: ").strip()
            id_membro = input("ID do Membro: ").strip()
            email = input("Email: ").strip()
            membro = Membro(nome, id_membro, email)
            biblioteca.adicionar_membro(membro)
        elif opcao == "2":
            id_membro = input("ID do membro a remover: ").strip()
            biblioteca.remover_membro(id_membro)
        elif opcao == "3":
            biblioteca.listar_membros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_emprestimos(biblioteca):
    """Menu para empréstimos e devoluções"""
    while True:
        print("\n--- Empréstimos e Devoluções ---")
        print("1. Emprestar Livro")
        print("2. Devolver Livro")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            isbn = input("ISBN do livro: ").strip()
            id_membro = input("ID do membro: ").strip()
            biblioteca.emprestar_livro(isbn, id_membro)
        elif opcao == "2":
            isbn = input("ISBN do livro a devolver: ").strip()
            biblioteca.devolver_livro(isbn)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_buscar(biblioteca):
    """Menu para buscar livros"""
    while True:
        print("\n--- Buscar Livros ---")
        print("1. Buscar por Título")
        print("2. Buscar por Autor")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = input("Digite o título (ou parte dele): ").strip()
            biblioteca.buscar_livro_por_titulo(titulo)
        elif opcao == "2":
            autor = input("Digite o autor (ou parte do nome): ").strip()
            biblioteca.buscar_livro_por_autor(autor)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def menu_relatorios(biblioteca):
    """Menu para relatórios"""
    while True:
        print("\n--- Relatórios ---")
        print("1. Livros Disponíveis")
        print("2. Livros Emprestados")
        print("3. Todos os Livros")
        print("4. Todos os Membros")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            biblioteca.listar_livros_disponiveis()
        elif opcao == "2":
            biblioteca.listar_livros_emprestados()
        elif opcao == "3":
            biblioteca.listar_livros()
        elif opcao == "4":
            biblioteca.listar_membros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu_principal()
