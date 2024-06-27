package aula4.classes;

public class percorrendoArray {

	public static void main(String[] args) {
		int[] arrayNum = {87,68,52,5,49,83,45,12,64};
		int total = 0;
		//adiciona o valor de cada elemento ao total
		for(int i : arrayNum)
			total +=i;
		/*dessa forma o contador i em vez de ser o indice é o próprio valor do indice. Logo o rertorno do código é a soma de todos os valores do array*/
		System.out.printf("Total de elementos arrayNum: %d\n", total);
	}
}
