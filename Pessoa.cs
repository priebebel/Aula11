public class Pessoa
{
    public int ID { get; private set; }
    public string Nome { get; private set; }
    public List<Livro> Livros { get; private set; }

    public Pessoa(int id, string nome)
    {
        ID = id;
        Nome = nome;
        Livros = new List<Livro>();
    }

    public void PegarLivro(Livro livro)
    {
        Livros.Add(livro);
    }

    public void DevolverLivro(Livro livro)
    {
        Livros.Remove(livro);
    }
}