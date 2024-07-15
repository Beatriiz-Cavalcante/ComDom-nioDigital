package aula8.polimorfismo;

public class Mae {
	public String Nome;
	public String Sobrenome;
	public Mae(String nome, String sobrenome) {
		this.Nome = nome;
		this.Sobrenome = sobrenome;
	}
	public void Parir() {
		System.out.printf("%s %s é mãe", Nome, Sobrenome);
	}
}
