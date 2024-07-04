package aula6.metodos;

import java.util.Scanner;

public class calculadora {

	public static void main(String[] args) {
		CalcularMetodos calculo1 = new CalcularMetodos();
		System.out.println("Calculadora");
		Scanner input = new Scanner(System.in);
		System.out.println("Você vai fazer as operações com 2 ou 3 números?");
		int quantidade = input.nextInt();
		
		System.out.println("Digite um número: ");
		int num1 = input.nextInt();
		System.out.println("Digite outro número: ");
		int num2 = input.nextInt();
		int num3=0;
		if (quantidade == 3) {
			System.out.println("Digite outro número: ");
			num3 = input.nextInt();
		}
		
		int controle = 1;
		while(controle>0 || controle<5) {
			System.out.println("Informe qual operação você deseja realizar\n"
					+ "1-Adição\n"
					+ "2-Subtração\n"
					+ "3-Multiplicação\n"
					+ "4-Divisão\n"
					+ "5-Encerrar");
			controle = input.nextInt();
			if(controle ==1) {
				if (quantidade ==2) {
					System.out.println(calculo1.somar(num1,num2));
				} else if (quantidade==3) {
					System.out.println(calculo1.somar(num1,num2, num3));
				}
				
			} else if (controle == 2) {
				if (quantidade ==2) {
					System.out.println(calculo1.subtracao(num1,num2));
				} else if (quantidade==3) {
					System.out.println(calculo1.subtracao(num1,num2, num3));
				}
			} else if (controle ==3) {
				if (quantidade ==2) {
					System.out.println(calculo1.multiplicacao(num1,num2));
				} else if (quantidade==3) {
					System.out.println(calculo1.multiplicacao(num1,num2, num3));
				}
			} else if (controle == 4) {
				if (quantidade ==2) {
					System.out.println(calculo1.divisao(num1,num2));
				} else if (quantidade==3) {
					System.out.println(calculo1.divisao(num1,num2, num3));
				}
			} else if (controle == 5) {
				System.out.println("Programa encerrado");
				break;
			} else {
				System.out.println("Número inválido");
			}
		}
	}

}
