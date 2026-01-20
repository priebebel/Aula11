# Aula11 - Sistema de Biblioteca

Sistema simples de gerenciamento de biblioteca desenvolvido durante a Aula 11.

## Descrição

Este é um sistema de biblioteca completo implementado em Python que permite:

- **Gerenciar Livros**: Adicionar, remover e listar livros
- **Gerenciar Membros**: Cadastrar e remover membros da biblioteca
- **Empréstimos e Devoluções**: Controlar o empréstimo e devolução de livros
- **Buscar Livros**: Buscar livros por título ou autor
- **Relatórios**: Visualizar livros disponíveis, emprestados e estatísticas

## Características

- Interface de menu interativa no terminal
- Controle de disponibilidade de livros
- Sistema de prazos de empréstimo (14 dias por padrão)
- Validações para evitar erros (livros duplicados, empréstimos inválidos, etc.)
- Busca flexível por título e autor
- Relatórios detalhados

## Como Usar

### Requisitos

- Python 3.6 ou superior

### Executando o Sistema

```bash
python biblioteca.py
```

### Menu Principal

O sistema apresenta um menu interativo com as seguintes opções:

1. **Gerenciar Livros**
   - Adicionar novos livros
   - Remover livros existentes
   - Listar todos os livros

2. **Gerenciar Membros**
   - Cadastrar novos membros
   - Remover membros
   - Listar todos os membros

3. **Empréstimos e Devoluções**
   - Emprestar livros para membros
   - Registrar devolução de livros

4. **Buscar Livros**
   - Buscar por título
   - Buscar por autor

5. **Relatórios**
   - Livros disponíveis
   - Livros emprestados (com data de devolução)
   - Todos os livros
   - Todos os membros

## Exemplo de Uso

```python
# Exemplo de uso programático
from biblioteca import Biblioteca, Livro, Membro

# Criar biblioteca
bib = Biblioteca("Minha Biblioteca")

# Adicionar livros
livro1 = Livro("1984", "George Orwell", "978-0451524935", "1949")
livro2 = Livro("Dom Casmurro", "Machado de Assis", "978-8525406194", "1899")
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

# Adicionar membros
membro1 = Membro("João Silva", "001", "joao@email.com")
bib.adicionar_membro(membro1)

# Emprestar livro
bib.emprestar_livro("978-0451524935", "001")

# Listar livros disponíveis
bib.listar_livros_disponiveis()

# Devolver livro
bib.devolver_livro("978-0451524935")
```

## Estrutura do Código

- `Livro`: Classe que representa um livro com título, autor, ISBN, ano de publicação e status
- `Membro`: Classe que representa um membro da biblioteca
- `Biblioteca`: Classe principal que gerencia todo o sistema
- `menu_principal()`: Interface de menu interativa
- Funções auxiliares de menu para cada módulo

## Funcionalidades Técnicas

- Armazenamento em memória usando dicionários Python
- Validações de entrada e saída
- Sistema de datas usando datetime
- Prazo de empréstimo configurável
- Mensagens de erro informativas

## Autor

Desenvolvido durante a Aula 11 de programação.