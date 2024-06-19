package aula2;

import java.util.Scanner;

public class numMaior {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int num1;
		int num2;
		int num3;
		System.out.println("Digite um número: ");
		num1 = input.nextInt();
		System.out.println("Digite outro número: ");
		num2 = input.nextInt();
		System.out.println("Digite outro número: ");
		num3 = input.nextInt();
		if (num1 > num2) {
			if(num1> num3) {
				System.out.printf("O número %d é maior do que %d e %d", num1, num3, num2);
			} else {
				System.out.printf("O número %d é maior do que %d e %d", num3, num2, num1);
			}
		} else {
			if (num2 > num3) {
				System.out.printf("O número %d é maior do que %d e %d", num2, num3, num1);
			} else {
				System.out.printf("O número %d é maior do que %d e %d", num3, num2, num1);
			}
		}

	}

}
