import java.util.Scanner;

public class Bestfit {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the block size: ");
        int m = sc.nextInt();
        int[] blocksize = new int[m];

        System.out.print("Enter the process size: ");
        int n = sc.nextInt();
        int[] processSize = new int[n];
        int[] allocation = new int[n];

        for (int i = 0; i < m; i++) {
            System.out.print("Enter the block " + (i + 1) + " size: ");
            blocksize[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            System.out.print("Enter the process " + (i + 1) + " size: ");
            processSize[i] = sc.nextInt();
        }
        sc.close();

        for (int i = 0; i < n; i++) {
            int bestFitIndex = -1;
            for (int j = 0; j < m; j++) {
                if (blocksize[j] >= processSize[i] && (bestFitIndex == -1 || blocksize[j] < blocksize[bestFitIndex])) {
                    bestFitIndex = j;
                }
            }
            if (bestFitIndex != -1) {
                allocation[i] = bestFitIndex;
                blocksize[bestFitIndex] -= processSize[i];
            }
        }
        
        System.out.println("\nProcess No.\tProcess Size\tBlock no.");
        for (int i = 0; i < n; i++) {
            System.out.print(" " + (i + 1) + "\t\t" + processSize[i] + "\t\t");
            if (allocation[i] != -1)
                System.out.print(allocation[i] + 1);
            else
                System.out.print("Not Allocated");
            System.out.println();
        }
    }
}
