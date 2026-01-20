var biblioteca = new Biblioteca();

// 5º Passo - Adicione livros na lista da biblioteca
biblioteca.CadastrarLivro(new Livro(1001, "O Pequeno Príncipe"));
biblioteca.CadastrarLivro(new Livro(1002, "Dom Casmurro"));
biblioteca.CadastrarLivro(new Livro(1003, "Clean Code"));
biblioteca.CadastrarLivro(new Livro(1004, "Harry Potter e a Pedra Filosofal"));

int proximoIdPessoa = 1;

while (true)
{
    Console.WriteLine();
    Console.WriteLine("=== SISTEMA DE BIBLIOTECA ===");
    Console.WriteLine("1 - Listar livros");
    Console.WriteLine("2 - Emprestar livro");
    Console.WriteLine("3 - Sair");
    Console.Write("Escolha uma opção: ");

    var opcao = Console.ReadLine();

    if (opcao == "1")
    {
        Console.WriteLine();
        Console.WriteLine("=== LISTA DE LIVROS ===");
        biblioteca.ListarLivros();
    }
    else if (opcao == "2")
    {
        Console.WriteLine();
        Console.WriteLine("=== EMPRÉSTIMO DE LIVRO ===");

        // Registrar locatário
        Console.Write("Digite o nome do locatário: ");
        var nome = (Console.ReadLine() ?? "").Trim();

        if (string.IsNullOrWhiteSpace(nome))
        {
            Console.WriteLine("Nome inválido. Operação cancelada.");
            continue;
        }

        var pessoa = new Pessoa(proximoIdPessoa, nome);
        proximoIdPessoa++;
        biblioteca.CadastrarUsuario(pessoa);

        // Escolher livro
        Console.WriteLine();
        Console.WriteLine("Por favor, escolha o livro desejado (pelo Tombo):");
        biblioteca.ListarLivros();

        Console.Write("Digite o Tombo do livro: ");
        var entradaTombo = Console.ReadLine();

        if (!int.TryParse(entradaTombo, out int tombo))
        {
            Console.WriteLine("Tombo inválido. Operação cancelada.");
            continue;
        }

        var livroEscolhido = biblioteca.BuscarLivroPorTombo(tombo);

        if (livroEscolhido == null)
        {
            Console.WriteLine("Livro não encontrado. Operação cancelada.");
            continue;
        }

        if (livroEscolhido.Status == "Emprestado")
        {
            Console.WriteLine($"Não é possível emprestar. Livro já está emprestado para: {livroEscolhido.Locatario}");
            continue;
        }

        var emprestou = biblioteca.EmprestarLivro(livroEscolhido, pessoa);

        if (emprestou)
        {
            Console.WriteLine($"Empréstimo realizado com sucesso: \"{livroEscolhido.Titulo}\" para {pessoa.Nome}");
        }
        else
        {
            Console.WriteLine("Não foi possível emprestar o livro.");
        }
    }
    else if (opcao == "3")
    {
        Console.WriteLine("Saindo...");
        break;
    }
    else
    {
        Console.WriteLine("Opção inválida. Tente novamente.");
    }
}
