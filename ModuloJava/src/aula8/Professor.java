package aula8;

public class Professor extends Pessoa {

	public Professor(String nome, String cpf, String telefone, double Salario, String disciplina) {
		super(nome,cpf,telefone);
		this.Salario = Salario;
		this.disciplina = disciplina;
	}
	public double Salario;
	public String disciplina;
}
