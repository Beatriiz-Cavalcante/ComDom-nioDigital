package aula8;

public abstract class Pessoa {
	public String nome;
	public String CPF;
	public String telefone;
	
	public Pessoa(String nome, String cpf, String telefone) {
		this.nome = nome;
		this.CPF = cpf;
		this.telefone = telefone;
	}

	//classe abstrata não deve ser instanciada
}
