package aula3;

public class impar100 {
	/*Escreva um aplicativo em java que mostre todos os números pares e ímpares de 1 até 100, separando por linhas*/
	public static void main(String[] args) {
		int contador = 1;
		System.out.println("Os números ímpares entre 0 e 100 são:");
		while (contador <= 100) {
			if (contador%2!=0) {
				System.out.print(contador + " ");
			} 
			contador++;
		}
		contador=1;
		System.out.println("\nOs números pares entre 0 e 100 são:");
		while (contador <= 100) {
			if (contador%2==0) {
				System.out.print(contador + " ");
			} 
			contador++;
		}
	}
}
