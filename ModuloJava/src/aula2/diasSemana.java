package aula2;

import java.util.Scanner;

public class diasSemana {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num;
		System.out.println("Digite um número: ");
		num = input.nextInt();
		if (num == 1) {
			System.out.printf("O número %d corresponde ao Domingo", num);
		} else if (num == 2) {
			System.out.printf("O número %d corresponde a segunda-feira", num);
		} else if (num == 3) {
			System.out.printf("O número %d corresponde a terça-feira", num);
		} else if (num == 4) {
			System.out.printf("O número %d corresponde a quarta-feira", num);
		} else if (num == 5) {
			System.out.printf("O número %d corresponde a quinta-feira", num);
		} else if (num == 6) {
			System.out.printf("O número %d corresponde a sexta-feira", num);
		} else if (num == 7) {
			System.out.printf("O número %d corresponde a sabado", num);
		} else {
			System.out.printf("Nenhum dia da semana corresponde a %d ", num);
		}
   }
}
