

// QUESTÃO 4255
// "2 números em ordem crescente - Adp."
// NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


import java.util.Scanner;

public class ex23 { //HuxleyCode no lugar do ex23
  public static void main(String args[]) {
     Scanner scanner = new Scanner(System.in);

        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        
        if (num1 < num2) {
            System.out.printf("%d\n", num1);
            System.out.printf("%d\n", num2);
        } else {
            System.out.printf("%d\n", num2);
            System.out.printf("%d\n", num1);
        }
        
        scanner.close();
  }
}