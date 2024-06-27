package aula4.classes;

import java.util.Scanner;
public class alunosArray {
/*Escreva um código que receva uma nota de 5 alunos, guarde todas num array notas. Depois calcule a média da turma*/
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		double notas[] = new double[6];
		double soma = 0;
		for(int i=1;i<6;i++) {
			System.out.printf("Informe a nota do aluno %d", i);
			notas[i] = input.nextDouble();
			soma = soma + notas[i];
		}
		System.out.print("As notas da turma são:\n");
		for(int i=1;i<6;i++) {
			System.out.print(notas[i] + " ");
		}
		
		double media = soma / 5;
		System.out.printf("\nA média da turma é: %.2f", media);
	}

}
