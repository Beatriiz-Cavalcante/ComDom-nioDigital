package aula6;

public class ClassePessoa {
	String nome;
	public void comer() {
		System.out.printf("%s Está comendo", nome);
		//se o método não retorna nada é preciso colocar 'void' na escrita da criação.
		//Para os métodos que retornam algo, é necessário especificar o tipo do retorno na escrita da criação
		/*Exemplo:
		 * int idade(){
		 * 	return 22;
		 * }*/
	}
}
