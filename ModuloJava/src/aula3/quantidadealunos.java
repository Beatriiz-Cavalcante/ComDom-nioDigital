package aula3;

import java.util.Scanner;
public class quantidadealunos {

	public static void main(String[] args) {
		/*Escreva um programa que pergunte ao usuário quantos alunos tem na sala dele. Em seguida, através de um laço while, pede
		 * ao usuário para que digite as notas de todos os alunos da sala, um por vez
		 * por fim o programamostra a média aritmética da turma*/
		System.out.println("Quantos alunos tem na sua sala?");
		Scanner input = new Scanner(System.in);
		int quantidade = input.nextInt();
		int contador = 1;
		double notas = 0;
		double media = 0;
		if (quantidade == 0) {
			System.out.println("Programa encerrado");
		} else {
			while(contador<=quantidade) {
				System.out.printf("Informe a nota do aluno %d", contador);
				double nota = input.nextDouble(); 
				notas = notas + nota;
				contador = contador + 1;
			}
			media = notas / quantidade;
			System.out.printf("A média da turma é %.2f", media);
		}
	}
}
