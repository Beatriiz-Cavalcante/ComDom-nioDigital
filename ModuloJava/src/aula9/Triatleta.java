package aula9;

public class Triatleta implements Corredor,Nadador, Ciclista {
	//atributos
	public String nome;
	//constutor
	public Triatleta(String nome) {
		this.nome = nome;
	}
	//sobrescrevendo os métodos das interfaces
	@Override
	public void Pedalar() {
		System.out.printf("%s pedala\n", nome);
	}

	@Override
	public void Nadar() {
		System.out.printf("%s nada\n", nome);
	}

	@Override
	public void Correr() {
		System.out.printf("%s corre\n", nome);
	}
	
	public void Descansar() {
		System.out.printf("%s também descansa\n", nome);
	}
}
