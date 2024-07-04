package aula6;

public class ClasseTeste {
	public static void main(String[] args) {
		ClassePessoa aluno01 = new ClassePessoa();
		aluno01.nome = "Bibs";
		System.out.println(aluno01.nome);
		aluno01.comer();
		
		ClassePessoa aluno02 = new ClassePessoa();
		aluno02.nome = "Trizz";
		System.out.println(aluno02.nome);
	}
}