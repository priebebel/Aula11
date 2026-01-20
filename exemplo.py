"""
Exemplo de uso do Sistema de Biblioteca
Demonstra o uso programático das classes
"""

from biblioteca import Biblioteca, Livro, Membro

def demo():
    """Demonstração do sistema de biblioteca"""
    
    print("="*60)
    print("  DEMONSTRAÇÃO DO SISTEMA DE BIBLIOTECA")
    print("="*60)
    
    # Criar a biblioteca
    print("\n1. Criando a biblioteca...")
    bib = Biblioteca("Biblioteca Central")
    print(f"   ✓ Biblioteca '{bib.nome}' criada com sucesso!")
    
    # Adicionar livros
    print("\n2. Adicionando livros ao acervo...")
    livros = [
        Livro("1984", "George Orwell", "978-0451524935", "1949"),
        Livro("Dom Casmurro", "Machado de Assis", "978-8525406194", "1899"),
        Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-0544003415", "1954"),
        Livro("Cem Anos de Solidão", "Gabriel García Márquez", "978-0307474728", "1967"),
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-0156012195", "1943"),
    ]
    
    for livro in livros:
        bib.adicionar_livro(livro)
    
    # Adicionar membros
    print("\n3. Cadastrando membros...")
    membros = [
        Membro("João Silva", "001", "joao.silva@email.com"),
        Membro("Maria Santos", "002", "maria.santos@email.com"),
        Membro("Pedro Oliveira", "003", "pedro.oliveira@email.com"),
    ]
    
    for membro in membros:
        bib.adicionar_membro(membro)
    
    # Listar todos os livros
    print("\n4. Listando todos os livros do acervo:")
    bib.listar_livros()
    
    # Listar todos os membros
    print("\n5. Listando todos os membros:")
    bib.listar_membros()
    
    # Realizar empréstimos
    print("\n6. Realizando empréstimos...")
    bib.emprestar_livro("978-0451524935", "001")  # 1984 para João
    bib.emprestar_livro("978-8525406194", "002")  # Dom Casmurro para Maria
    bib.emprestar_livro("978-0544003415", "001")  # Senhor dos Anéis para João
    
    # Listar livros disponíveis
    print("\n7. Livros disponíveis após empréstimos:")
    bib.listar_livros_disponiveis()
    
    # Listar livros emprestados
    print("\n8. Livros emprestados:")
    bib.listar_livros_emprestados()
    
    # Buscar livros
    print("\n9. Buscando livros por título ('Senhor'):")
    bib.buscar_livro_por_titulo("Senhor")
    
    print("\n10. Buscando livros por autor ('Machado'):")
    bib.buscar_livro_por_autor("Machado")
    
    # Devolver um livro
    print("\n11. Devolvendo um livro...")
    bib.devolver_livro("978-0451524935")  # João devolve 1984
    
    # Status final
    print("\n12. Status final dos livros:")
    bib.listar_livros()
    
    print("\n13. Status final dos membros:")
    bib.listar_membros()
    
    print("\n" + "="*60)
    print("  DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)


if __name__ == "__main__":
    demo()
