package aula7;

public class Aplicacao {

	public static void main(String[] args) {
		Carro c1 = new Carro();
		Carro c2 = new Carro("Azul");
		Carro c3 = new Carro("Cinza","ALgum motor", 30000.00);
		c1.cor = "vermelho";
		c1.motor = "Turbo diesel";
		c1.valor = 250000.00;
		c1.desligar();
		c1.ligar();
		c1.desligar();

	}

}
