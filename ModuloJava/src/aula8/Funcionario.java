package aula8;

public class Funcionario extends Pessoa{

	public Funcionario(String nome, String cpf, String telefone, double Salario, String cargo) {
		super(nome,cpf,telefone);
		this.salario = Salario;
		this.cargo = cargo;
	}
	public double salario;
	public String cargo;
}
