import java.util.*;

public class exp1 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    List<Character> Start = new ArrayList<Character>();
    List<Character> End = new ArrayList<Character>();
    for(int i =1;i<=3;i++)
    {
      Start.add('c');
      Start.add('m');
    }
    
    while (!Start.isEmpty() || End.size() == 6) {
      
      System.out.println("Enter number of people you want to send from left bank to right bank: ");
      int n1 = sc.nextInt();
      while (n1 > 0) {
        System.out.println("Enter 'c' or 'm' : ");
        char temp = sc.next().charAt(0);
        if (Start.contains(temp)) {
          Start.remove(Character.valueOf(temp));
          End.add(temp);

        } else {
          System.out.println("Invalid input");
          return;
        }
        n1--;

      }
      if (CheckCount(Start) && CheckCount(End)) {
        System.out.println("Successfully sent");
      } else {
        System.out.println("Failed");
        return;
      }
      if(End.size() == 6)
      {
        break;
      }
      System.out.println("Enter number of people you want to send from right bank to left bank: ");
      int n2 = sc.nextInt();
      while (n2 > 0) {

        System.out.println("Enter 'c' or 'm' : ");
        char temp = sc.next().charAt(0);
        if (End.contains(temp)) {
          Start.add(temp);
          End.remove(Character.valueOf(temp));
        } else {
          System.out.println("Invalid input");
          return;
        }

        n2--;
      }
      if (CheckCount(Start) && CheckCount(End)) {
        System.out.println("Successfully sent");
      } else {
        System.out.println("Failed");
        return;
      }

    }
    System.out.println("Game successfully completed");

  }

  

  public static Boolean CheckCount(List<Character> Bank) {
    int countC = 0;
    int countM = 0;
    for (char i : Bank) {
      if (i == 'c') {
        countC++;
      } else {
        countM++;
      }
    }
    
    System.out.println(countC);
    System.out.println(countM);
    if(countM==0)
    {
      return true;
    }
    return countC <= countM;

  }
}