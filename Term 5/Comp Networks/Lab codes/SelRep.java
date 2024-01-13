import java.util.*;

public class SelRep {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter the Window Size: ");
        int window = sc.nextInt();
        System.out.println("Enter number of frames to be sent : ");
        int n = sc.nextInt();
        for (int j = 0; j < n; j++) {
            System.out.println("Frame " + j + " has been transmitted");
        }
        for (int k = 0; k < window; k++) {
            System.out.println("Enter 1 if any frames are missing ");
            System.out.println("Enter 0 if no frames are missing ");
            int ans = sc.nextInt();
            if (ans == 1) {
                System.out.println("enter the unreceived Acknowledgement number : ");
                int a = sc.nextInt();
                System.out.println("Frame " + a + " has been transmitted.");
            } else {
                break;
            }
        }
    }
}