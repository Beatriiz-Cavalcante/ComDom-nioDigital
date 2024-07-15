package aula8.polimorfismo;

public class Retangulo extends Formas {
	public Retangulo(double base, double altura) {
		super(base,altura);
	}
	public double Area(double base, double altura) {
		double resultado = base * altura;
		return resultado;
	}
	public double Perimetro(double base, double altura) {
		double resultado = 2 * (base + altura);
		return resultado;
	}

}
