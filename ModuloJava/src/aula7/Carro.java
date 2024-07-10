package aula7;

public class Carro {
	//atributos
	public String motor;
	public String cor;
	public double valor;
	private int verifica = 0;
	//metodo construtor
	public Carro(String Cor) {
		this.cor = cor;
	}
	public Carro(String Cor, String Motor, double Valor) {
		this.cor = cor;
		this.motor = motor;
		this.valor=valor;
	}
	public Carro() {
		//se identifica o método construtor de acordo com o nome, ele tem o mesmo nome da classe
	}
	public void ligar() {
		if (verifica ==1) {
			System.out.println("Carro já está ligado");
		} else {
			System.out.println("Carro ligado");
			verifica = 1;
		}
	}
	public void desligar() {
		if(verifica == 0) {
			System.out.println("Carro já está desligado");
		} else {
			System.out.println("Carro desligado");
			verifica = 0;
		}
	}
}
