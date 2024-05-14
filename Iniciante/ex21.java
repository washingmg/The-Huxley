

// QUESTÃO 178
// "Cometa"
// NÍVEL DE ACORDO COM O THE HUXLEY: INICIANTE


// import java.io.*; //ativar o import java.io
import java.util.*;

public class ex21 { //HuxleyCode
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    
    int numero = input.nextInt();
    int ano = 1986;
    while (ano < numero){
      ano += 76;
    }
    System.out.printf("%d", ano);
    input.close();
  }
}