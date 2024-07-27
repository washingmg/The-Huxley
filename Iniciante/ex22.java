

// QUESTÃO 3131
// "[AC3.2] - Divisibilidade"
// NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


import java.util.Scanner;

public class ex22 { // HuxleyCode no lugar de ex22
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int numero = scanner.nextInt();
    scanner.close();

    if ((numero % 4 == 0) && (numero % 7 == 0) && (numero % 5 != 0)) {
        System.out.println("sim");
    } else {
        System.out.println("nao");
    }
  }
}
