package aula8;

public class Aluno extends Pessoa{
		public Aluno(String nome, String cpf, String telefone, String matricula) {
			super(nome,cpf,telefone);
			this.Matricula = matricula;
		}
		public String Matricula;
	}