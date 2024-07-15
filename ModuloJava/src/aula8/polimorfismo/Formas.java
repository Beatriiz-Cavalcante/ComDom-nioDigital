package aula8.polimorfismo;

public abstract class Formas {
	public double base;
	public double altura;
	public Formas(double base, double altura) {
		this.base= base;
		this.altura=altura;
	}
	public double Area(double base, double altura) {
		return 0;
	}
	public double Perimetro(double base, double altura) {
		return 0;
	}
}
