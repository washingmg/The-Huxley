

//QUESTÃO 2797
//"Zerinho ou um"
//NÍVEL DE ACORDO COM O THE HUXLEY: FÁCIL


import java.util.Scanner;

public class ex14 { //Huxleycode
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        
        char resultado = zerinhoOuUm(A, B, C);
        System.out.println(resultado);
        
        scanner.close();
    }
    
    public static char zerinhoOuUm(int A, int B, int C) {
        if (A != B && A != C) {
            return 'A';
        } else if (B != A && B != C) {
            return 'B';
        } else if (C != A && C != B) {
            return 'C';
        } else {
            return '*';
        }
    }
}
