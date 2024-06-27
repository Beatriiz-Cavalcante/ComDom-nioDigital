package aula4.classes;

public class tamanhoArray {

	public static void main(String[] args) {
		int[] arrayUm = {12,3,5,68,9,6,73,44,456,65,321};
		int[] arrayDois = {43,42,4,8,55,21,2,45};
		
		if(arrayDois.length>8) {
			System.out.println("Tamanho do ArrayDois - Maior do que 8!");
		} else {
			System.out.println("Tamanho do arrayDois - menor ou  igual a 8!");
		}
		System.out.println("\nTamanho do arrayUm = "+arrayUm.length);

	}

}
