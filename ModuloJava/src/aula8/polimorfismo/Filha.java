package aula8.polimorfismo;

public class Filha extends Mae {

	public Filha(String nome, String sobrenome) {
		super(nome, sobrenome);
	}

	public void Parir() {
		System.out.printf("%s %s é filha", Nome, Sobrenome);
	}
	
}
