package lacoFor;

public class forEcontinue {

	public static void main(String[] args) {
		for(int i=0; i<100; i++) {
			if(i>50 && i<60) {
				continue;
			}
			//o continue faz com que a condição do if seja pulada. Logo o os números são printados de 1 a 100 execeto os números de 51 a 60.
			/*o break pára o laço de repetição de vez e o continue para de acordo com uma condição e depois volta*/
		System.out.println(i);
		}
	}
}
