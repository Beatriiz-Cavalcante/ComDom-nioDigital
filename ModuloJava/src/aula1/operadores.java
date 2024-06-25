package aula1;

public class operadores {
	public static void main(String[] args) {
		/*O sufixo o valor atual da variavel é usado na expressão antes
		 *  de ser incrementado ou decrementado*/
		int x = 10;
		System.out.println(x++);
		/*O prefixo a variavel é incrementada ou decrementada antes de 
		 * ser usada na expressão*/
		System.out.println(++x);
		System.out.println(x--);
		System.out.println(--x);
		
		//adição e incremento/decremento
			int a = 10;
			int b = 10;
			System.out.println( a++ + ++a); //10 + 12 = 22
			System.out.println( b++ + b++); // 10 + 11 = 21
		
		//boolean
			int c = 10;
			int d = -10;
			boolean e = true;
			boolean f = false;
			System.out.println(~c); // - 11 (inverte o sinal e subtrai com 1)
			System.out.println(~d); // 9 (inverte o sinal e subtrai com 1)
			System.out.println(!e); // false (oposto ao valor booleano)
			System.out.println(!f); // true
			
		//logicos
			int g = 3;
			int h = 4;
			int i = 7;
			
			System.out.println((!((g>h) && (g <i))));

	}
}
