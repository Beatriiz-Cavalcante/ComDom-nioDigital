package aula9;

import java.util.Scanner;
public class Testando {

	public static void main(String[] args) {
		Triatleta atleta1 = new Triatleta("Bibs");
		Scanner input = new Scanner(System.in);
		int contador = 0;
		while (contador<5) {
			System.out.println("Deseja acionar alguma ação do atleta?\n"
					+ "Digite 1 para Correr;\n"
					+ "Digite 2 para Nadar\n"
					+ "Digite 3 para Pedalar\n"
					+ "Digite 4 para Descansar\n"
					+ "Digite 5 para encerrar o programa.");
			contador = input.nextInt();
			if (contador < 1 || contador > 5 ) {
				while(contador <1 || contador>5) {
					System.out.println("Digite um número válido");
					contador = input.nextInt();
				}
			} else if(contador == 1) {
				atleta1.Correr();
			} else if (contador == 2) {
				atleta1.Nadar();
			} else if(contador == 3) {
				atleta1.Pedalar();
			} else if (contador == 4) {
				atleta1.Descansar();
			} else{
				break;
		    }
	}
	System.out.println("Programa encerrado");
 }
}
