package aula2;

/*Faça um programa que verifique se uma letra digitada é f ou m.
 *  Conforme a letra escrever f- feminino, m - masculino*/
import java.util.Scanner;

public class femMasc {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		char letra;
		System.out.print("Informe o seu gênero: ");
		letra = input.next().charAt(0);
		if (letra=='F' || letra == 'f') {
			System.out.printf("%S corresponde ao gênero feminino", letra);
		} else if (letra=='M' || letra == 'm') {
			System.out.printf("%S corresponde ao gênero masculino", letra);
		} else {
			System.out.printf("A letra %S não corresponde a nenhum gênero", letra);
		}
	}

}
