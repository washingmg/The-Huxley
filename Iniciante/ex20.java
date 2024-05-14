

// QUESTÃO 1065
// "Multiplo de 5"
// NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE



// import java.io.*; //ativar o import java.io
import java.util.*;

public class ex20 { //HuxleyCode no lugar do ex20
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    int valor = input.nextInt();

    if (valor % 5 == 0)
      System.out.println("Eh multiplo de 5");
    else
      System.out.println("Nao eh multiplo de 5");
    input.close();
  }
}