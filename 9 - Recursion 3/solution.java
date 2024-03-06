import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
public static final Scanner sc= new Scanner(System.in);
    // Complete the factorial function below.
    static int factorial(int n) {
        if(n<=1){
            return 1;
        }
        else{
            return n * factorial(n-1);
        }
    }
    public static void main(String agrs[]){
        int a=sc.nextInt();
        System.out.println(factorial(a));
    }
}
