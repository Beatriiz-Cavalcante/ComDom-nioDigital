package aula8.polimorfismo;

public class Triangulo extends Formas{
	public Triangulo(double base, double altura, double lado, double lado2) {
		super(base,altura);
		this.lado=lado;
		this.lado2=lado2;
	}
	public double lado;
	public double lado2;
	public double Area(double base, double altura) {
		double resultado = (base * altura)/2;
		return resultado;
	}
	public double Perimetro(double base, double lado, double lado2) {
		double resultado = base + lado + lado2;
		return resultado;
	}
}
