package desafios;

import java.util.Scanner;
public class delegacia {

	public static void main(String[] args) {
		/*Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
			“Telefonou para a vítima? “
			“Esteve no local do crime?”
			“Mora perto da vítima? “
			“Devia para a vítima? “
			“Já trabalhou com a vítima? “
			O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 
			questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.*/
		int c1=0;
		int c2=0;
		int c3=0;
		int c4=0;
		int c5=0;
		Scanner input = new Scanner(System.in);
		System.out.println("Início do interratório");
		System.out.println("Você telefonou para a vítima? \n1-Sim;\n2-Não;");
		int r1 = input.nextInt();
		if (r1 == 1) {
			c1 = 1;
		} else {
			c1 = 0;
		}
		System.out.println("Mora perto da vítima? \n1-Sim;\n2-Não;");
		int r2 = input.nextInt();
		if (r2 == 1) {
			c2 = 1;
		} else {
			c2 = 0;
		}
		System.out.println("Você telefonou para a vítima? \n1-Sim;\n2-Não;");
		int r3 = input.nextInt();
		if (r3 == 1) {
			c3 = 1;
		} else {
			c3 = 0;
		}
		System.out.println("Devia para a vítima? \n1-Sim;\n2-Não;");
		int r4 = input.nextInt();
		if (r4 == 1) {
			c4 = 1;
		} else {
			c4 = 0;
		}
		System.out.println("Já trabalhou com a vítima? \n1-Sim;\n2-Não;");
		int r5 = input.nextInt();
		if (r5 == 1) {
			c5 = 1;
		} else {
			c5 = 0;
		}
		int resultado;
		resultado = c1 + c2 + c3 + c4 +c5;
		if (resultado < 2) {
			System.out.print("Pessoa é inocente");
		} else if (resultado == 2) {
			System.out.print("Pessoa é suspeita");
		} else if ((resultado>2) && (resultado<5)) {
			System.out.print("Pessoa é cúmplice");
		} else if (resultado == 5) {
			System.out.print("Pessoa é assassina");
		}
	}

}
