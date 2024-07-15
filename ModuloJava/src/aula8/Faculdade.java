package aula8;

public class Faculdade {

	public static void main(String[] args) {
		Aluno vely = new Aluno("Vely","cpf dela","telefone dela", "123");
		//em vezz de colocar o parâmetro criado na própria classe entre parenteses pode-se escrever dessa forma -> vely.matricula = "123"
		Professor weligton = new Professor("Weligton","um cpf","ddd 081",5000,"Programação");
		Funcionario tia = new Funcionario("Algumatia","1234","081988265820",2000,"Tia da lanchonete");

		System.out.println("Instância Aluno");
		System.out.printf("Nome: %s\nCPF: %s\nTelefone: %s\nMatricula: %s",vely.nome, vely.CPF, vely.telefone, vely.Matricula);
		System.out.println("Instância Professor");
		System.out.printf("Nome: %s\nCPF: %s\nTelefone: %s\nSalario: %f\nCargo: %s",weligton.nome, weligton.CPF, weligton.telefone, weligton.Salario, weligton.disciplina);
		System.out.println("Instância Funcionario");
		System.out.printf("Nome: %s\nCPF: %s\nTelefone: %s\nSalario: %f\nCargo: %s",tia.nome, tia.CPF, tia.telefone, tia.salario, tia.cargo);
	}

}
