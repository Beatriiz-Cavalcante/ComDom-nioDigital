package aula5;

import java.util.StringTokenizer;

public class classeString {

	public static void main(String[] args) {
		char caracteres[] = {'a','b','c'};
		String texto = new String(caracteres);  //transformando um array em string
		System.out.println(texto);

		/*, string em java é considerado um objeto, portanto tem métodos*/
		
		/*replace - método para substituir*/
		String str = "Hello";
		String resultado = str.replace("l","W"); //o primeiro parâmetro é o que vai ser substituido e o segundo é o que vai substituir.
		System.out.println(resultado); //HeWWo
		
		/*Para concatenação de strings se usa o sinal +*/
		String str1 = "oi";
		String texto1 = str1 + " " + "Mundo";
		System.out.println(texto1); //oi Mundo
		
		/*substring - Para extrair um texto de uma String */
		String str2 = "Hello World";
		String resultado2 = str2.substring(6); //o parâmentro passado é de onde começará a divisão da string
		System.out.println(resultado2); //world
		
		String resultado3 = str2.substring(3, 8); //os parâmentros passados indicam onde começa e até onde vai a divisão
		System.out.println(resultado3); //lo wo
		
		/*toUpperCase - Para converter todos os caracteres para maiúsculo*/
		String str3 = "Hello";
		String resultado4 = str.toUpperCase();
		System.out.println(resultado4); //HELLO
		
		/*trim - Para retirar espaços em branco no início e no final de uma string*/
		String str4 = " Hello ";
		String resultado5 = str4.trim();
		System.out.println(str4); // Hello
		System.out.println(resultado5); //Hello
		
		/*charAt - Para extrair um caractere de uma string de acordo com a posição especificada*/
		String str5 = "Opa";
		char c = str5.charAt(1);
		System.out.println(c);
		
		/*Para comparar se duas strings são iguais, podemos usar o método equals. Existe também o método equalsIgnoreCase que compara
		duas strings ignorando maiúsculas e minúsculas. Esses dois métodos retornam como resultado um valor boolean.*/
		
		String s1 = "Hello";
		String s2 = "HELLO";
		boolean b1 = s1.equals("Hello");
		System.out.println(b1);
		boolean b2 = s1.equals(s2);
		System.out.println(b2);
		boolean b3 = s1.equalsIgnoreCase(s2);
		System.out.println(b3);
		boolean b4 = s1.equalsIgnoreCase("azul");
		System.out.println(b4);
		
		/*length - Para rerornar o número de caracteres de uma array*/
		String s = "abc";
		int tam = s.length();
		System.out.println(tam); //3
		
		/*indexOf - Identificando a posição de caracteres ou substrings em uma String (o primeiro)
		 * lastIndexOf -Para a última aparição */
		String str6 = "Hello World World2";
		int pos = str6.indexOf("l"); //o parâmetro a ser consultado
		System.out.println(pos); //2 
		int pos2 = str6.lastIndexOf("l");
		System.out.println(pos2); //15
		
		/*Para comparar a sequência de caracteres de uma string
		 * endsWith - para o fim
		 * startsWith - para o início*/
		String valor = "CDD - Java";
		System.out.println(valor.endsWith("Java"));
		System.out.println(valor.startsWith("C"));
		System.out.println(valor.startsWith("DD",1)); //o número passado como parâmetro serve para indicar o índice em que vai começar a verificação 
		
		
		/*StringTokenizer*/
		StringTokenizer exemplo = new StringTokenizer("O mundo não é mais o mesmo mas não iremos desistir nunca"); 
		System.out.println(exemplo.countTokens()); //conta o número de palavras
		
		
		
		
		
		
		
		
	}

}
