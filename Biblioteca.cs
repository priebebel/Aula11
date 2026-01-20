public class Biblioteca
{
    public List<Livro> Livros { get; private set; }
    public List<Pessoa> Pessoas { get; private set; }

    public Biblioteca()
    {
        Livros = new List<Livro>();
        Pessoas = new List<Pessoa>();
    }

    public void CadastrarLivro(Livro livro)
    {
        Livros.Add(livro);
    }

    public void CadastrarUsuario(Pessoa pessoa)
    {
        Pessoas.Add(pessoa);
    }

    public void ListarLivros()
    {
        if (Livros.Count == 0)
        {
            Console.WriteLine("Nenhum livro cadastrado.");
            return;
        }

        foreach (var livro in Livros)
        {
            Console.WriteLine(livro.ToString());
        }
    }

    public Livro? BuscarLivroPorTombo(int tombo)
    {
        return Livros.FirstOrDefault(l => l.Tombo == tombo);
    }

    public bool EmprestarLivro(Livro livro, Pessoa pessoa)
    {
        var ok = livro.Emprestar(pessoa.Nome);
        if (!ok) return false;

        pessoa.PegarLivro(livro);
        return true;
    }
}