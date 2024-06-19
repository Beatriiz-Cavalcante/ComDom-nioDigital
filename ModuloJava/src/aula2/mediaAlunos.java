package aula2;

import java.util.Scanner;

public class mediaAlunos {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		double nota1;
		double nota2;
		double media;
		System.out.println("Digite a nota 1: ");
		nota1 = input.nextDouble(); 
		System.out.println("Digite a nota 2: ");
		nota2 = input.nextDouble();
		media = (nota1 + nota2)/2;
		if(media>=7) {
			System.out.printf("A média do aluno é %.2f Logo, ele está aprovado", media);
		} else if (media<7 && media>3) {
			System.out.printf("A média do aluno é %.2f Logo, ele está em recuperação", media);
		} else {
			System.out.printf("A média do aluno é %.2f Logo, ele está reprovado", media);
		}
	}

}
