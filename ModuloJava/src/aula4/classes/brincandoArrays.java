package aula4.classes;

import java.util.Arrays; //biblioteca para utilizar um método próprio de arrays
public class brincandoArrays {

	public static void main(String[] args) {
		int num[]= {20,17,22,16,36,57,33};
		//imprimir o array inverso na tela
		for(int i = 6; i>=0; i--) {
			System.out.print(num[i] + " ");
	     }
		
		System.out.println();
		//Guardar o reverso em outro array
		int num2[] = new int[7];
		for(int i=6; i>=0; i--) {
			num2[i] = num[6-i];
			System.out.print(num2[i] + " ");
		}
		
		System.out.println();
		//Imprimir em ordem crescente
		Arrays.sort(num);  //sintaxe da utilização do método sort que coloca em ordem crescente
		for (int i = 0; i < num.length; i++) {
		    System.out.print(num[i] + " ");
		}
		
		//Refaça o primeiro sem inverter o for
	}

}     
