package aula2;

import java.util.Scanner;

public class scannerEntrada {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String nome;
		int idade;
		System.out.print("Digite seu nome: ");
		nome = input.nextLine();
		System.out.println("Digite a sua idade: ");
		idade = input.nextInt();
		System.out.print(nome + " " + idade);
		System.out.printf("\n Olá %s, sua idade é %d", nome, idade);
	}

}
