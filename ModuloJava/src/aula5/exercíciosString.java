package aula5;

import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class exercíciosString {

	public static void main(String[] args) {
		
		/*Faça um programa que remova os espaços do inicio e do fim do texto*/
		String texto = " Texto para retirar espaços no início e no fim ";
		String resultado = texto.trim();
		System.out.println(resultado);

		/*faça um programa, que a partir de um texto digitado pelo usuário, conte o número de caracteres*/
		System.out.println("Digite uma frase:");
		Scanner input = new Scanner(System.in);
		String frase = input.nextLine();
		StringTokenizer frase2 = new StringTokenizer(frase);
		System.out.println("A frase dada tem " + frase2.countTokens() + " palavras");
	
		/*Compare os 2 textos abaixo e diga se são iguais*/
		String texto01 = "Será que são iguais?";
		String texto02 = "Será que são iguais?";
		boolean b1 = texto01.equals(texto02);
		if (b1){
			System.out.println("São iguais");
		} else {
			System.out.println("São diferentes");
		}
		
		/*Faça um programa que receba de um usuário, um texto e exiba esse texto em letras maiúsculas*/
		System.out.println("O texto dado com letras maiúsculas");
		System.out.println(frase.toUpperCase()); //usando o texto recebido no item 2
		
		/*dado o array a seguir {"a","vida,"é","bela"} faça um programa que crie uma string com o texto retirado do array e imprima em maiusculo*/
		
		//char caracteres[] = {'a','vida', 'é','bela'};
		//String naoEarray = new String(caracteres);  
		//System.out.println(naoEarray.toUpperCase());

		String[] palavras = {"a", "vida", "é", "bela"};
		String pratexto = (Arrays.toString(palavras)).replace(",", "").replace("[", "").replace("]", "");
		System.out.println(pratexto.toUpperCase());

		String primeiro = pratexto.substring(9);
		String segundo = pratexto.substring(7,8);
		String terceiro = pratexto.substring(0,1);
		String quarto = pratexto.substring(2,7);
		System.out.print(primeiro + " " + segundo + " " + terceiro + " " + quarto);
		
		
	}

}
