package aula8.polimorfismo;

public class teste {
	public static void main(String[] args) {
		//exemplo de polimorfismo de sobrescrista
		Mae Lucia = new Mae("Lucia", "Menezes");
		Lucia.Parir();
		System.out.println();
		Filha Bia = new Filha("Bia", "Menezes");
		Bia.Parir();
		System.out.println();
		
		//polimorfismo de sobrecarga
		/*A sobrecarga permite que métodos com o mesmo nome, mas com diferentes tipos de parâmetros ou um número diferente de parâmetros, sejam definidos 
		 * na mesma classe. A decisão de qual método será chamado é feita pelo compilador com base nos tipos e na quantidade de argumentos passados durante 
		 * a chamada do método.*/
		
		//exemplo de polimorfismo de sobrescrita
		Triangulo t1 = new Triangulo(10,5,5,5);
		double areat = t1.Area(10, 5);
		double perimt = t1.Perimetro(10,5,5);
		System.out.printf("A área do triangulo é: %.2f\nO perímetro do triangulo é: %.2f", areat, perimt);
		
		System.out.println();
		
		Retangulo r1 = new Retangulo(10,5);
		double arear = r1.Area(10, 5);
		double perimr = r1.Perimetro(10, 5);
		System.out.printf("A área do retangulo é: %.2f\nO perímetro do retangulo é: %.2f", arear, perimr);
	}

}
