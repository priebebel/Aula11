

public class Livro
{
    public int Tombo { get; private set; }
    public string Titulo { get; private set; }
    public string Status { get; private set; } // "Disponível" ou "Emprestado"
    public string Locatario { get; private set; }

    public Livro(int tombo, string titulo)
    {
        Tombo = tombo;
        Titulo = titulo;
        Status = "Disponível";
        Locatario = "";
    }

    public bool Emprestar(string nomeLocatario)
    {
        if (Status == "Emprestado") return false;

        Status = "Emprestado";
        Locatario = nomeLocatario;
        return true;
    }

    public void Devolver()
    {
        Status = "Disponível";
        Locatario = "";
    }

    public override string ToString()
    {
        var extra = Status == "Emprestado" ? $" (Locatário: {Locatario})" : "";
        return $"{Tombo} - {Titulo} | {Status}{extra}";
    }
}