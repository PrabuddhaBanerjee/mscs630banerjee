import java.util.Scanner;
public class KargoTest {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    String s1 = input.nextLine();
    String s2 = input.nextLine();
    System.out.println(checkOneToOne(s1,s2));
    input.close();
  }
  public static boolean checkOneToOne(String s1, String s2){
    boolean flag = true;
    if(s1.length()>s2.length())
      return flag = false;
    for(int i =0; i<s1.length(); i++){
      for(int j = i+1; j<s1.length(); j++){
        if(s1.charAt(i)==s1.charAt(j))
          flag=false;
      }
    }
    return flag;
  }
}
