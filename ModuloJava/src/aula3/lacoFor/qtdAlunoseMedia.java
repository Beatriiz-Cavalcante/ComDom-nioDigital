package lacoFor;

import java.util.Scanner;
public class qtdAlunoseMedia {

	public static void main(String[] args) {
		/*Escreva um programa que solicite a quantidade de alunos de uma sala e depois solicite uma nota para cada aluno, imprimindo
		 * no final a média da sala*/ 
		System.out.println("Quantos alunos tem na sua sala?");
		Scanner input = new Scanner(System.in);
		int quantidade = input.nextInt();
		double notas = 0;
		double media = 0;
		for(int c = 0; c<quantidade;c++) {
			System.out.printf("Informe a nota do aluno %d", quantidade);
			double nota = input.nextDouble();
			notas = notas + nota;
		}
		media = notas / quantidade;
		System.out.print(notas);
		System.out.printf("A média da turma é %.2f", media);
	}

}
