package aula4.classes;

import java.util.Scanner;
public class valoresArray {

	public static void main(String[] args) {
		/*Para cada conjunto de valores abaixo, escreva o código Java, usando laço(s), que preencha um array com os valores:
		 * a- 10 9 8 7 6 5 4 3 2 1
		 * b- 1 4 9 16 25 36 49 64 81 100
		 * c- 1 2 3 4 5 10 20 30 40 50
		 * d- 3 4 7 12 19 28 39 52 67 84*/
		
		//a
		int array1[] = new int[11];
		Scanner input = new Scanner(System.in);
		for(int i = 1; i<11; i++) {
			System.out.printf("Informe o valor do array1 no indice %d", i);
			array1[i] = input.nextInt();
		}
		System.out.printf("O array1 ficou com os seguintes valores:");
		for(int i = 1; i<11; i++) {
			System.out.print(array1[i] + " ");
		}
		
		//b
		int array2[] = new int[11];
		for(int i = 1; i<11; i++) {
			System.out.printf("Informe o valor do array2 no indice %d", i);
			array2[i] = input.nextInt();
		}
		System.out.printf("O array2 ficou com os seguintes valores:");
		for(int i = 1; i<11; i++) {
			System.out.print(array2[i] + " ");
		}
		
		
	}

}
