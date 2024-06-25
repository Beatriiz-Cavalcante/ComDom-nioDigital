package lacoFor;

public class classeFor {

	public static void main(String[] args) {
		//exemplo1
		for (int i =0; i<10; i++) {
			System.out.println("Olá!");
		}
		//exemplo2
		for(int i = 0; i<100; i++) {
			if(i%3==0) {
				System.out.printf("Achei um número divisível por 3 entre x e y");
				System.out.println(i);
				break;
			}
		}

	}

}
