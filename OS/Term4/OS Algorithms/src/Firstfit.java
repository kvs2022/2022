//import java.util.Scanner;
//public class Firstfit {
//	public static void main(String args[]) {
//		Scanner sc = new Scanner(System.in);
//		System.out.println("Enter the block size");
//		int a=sc.nextInt();
//		int blocksize[]=new int [a];
//		System.out.println("enter the process size");
//		int b=sc.nextInt();
//		int processsize[]=new int[b];
//		int allocation[]=new int[b];
//		
//		
//		for (int i=0;i<a;i++)
//		{
//			System.out.println("Enter the block size");
//			blocksize[i]=sc.nextInt();
//		}
//		for (int i=0;i<b;i++) {
//			System.out.println("Enter the process size");
//			processsize[i]=sc.nextInt();
//		}
//		sc.close();
//		
//		for (int i=0; i<allocation.length;i++)
//		{
//			allocation[i]=-1;
//		}
//		for (int i=1; i<b;i++)
//		{
//			for (int j=1; j<b; j++)
//			{
//				if (blocksize[j]>=processsize[i])
//				{
//					allocation[i]=j;
//					blocksize[j]-=processsize[i];
//					break;
//				}
//			}
//		}
//		System.out.println("\nProcess No.\tProcess Size\tBlock no.");
//	    for (int i = 0; i < b; i++)
//	    {
//	        System.out.print(" " + (i+1) + "\t\t" +
//	                         processsize[i] + "\t\t");
//	        if (allocation[i] != -1)
//	            System.out.print(allocation[i] + 1);
//	        else
//	            System.out.print("Not Allocated");
//	        System.out.println();
//	    }   
//		
//	}
//	
//
//}


// import java.util.Scanner;
// public class Firstfit {
// 	public static void main(String args[]) {
// 		Scanner sc = new Scanner(System.in);
// 		System.out.println("Enter the block size");
// 		int a=sc.nextInt();
// 		int blocksize[]=new int [a];
// 		System.out.println("enter the process size");
// 		int b=sc.nextInt();
// 		int processsize[]=new int[b];
// 		int allocation[]=new int[b];
		
		
// 		for (int i=0;i<a;i++)
// 		{
// 			System.out.println("Enter the block size");
// 			blocksize[i]=sc.nextInt();
// 		}
// 		for (int i=0;i<b;i++) {
// 			System.out.println("Enter the process size");
// 			processsize[i]=sc.nextInt();
// 		}
// 		sc.close();
		
// 		for (int i=0; i<allocation.length;i++)
// 		{
// 			allocation[i]=-1;
// 		}
// 		for (int i=1; i<b;i++)
// 		{
// 			for (int j=1; j<b; j++)
// 			{
// 				if (blocksize[j]>=processsize[i])
// 				{
// 					allocation[i]=j;
// 					blocksize[j]-=processsize[i];
// 					break;
// 				}
// 			}
// 		}
// 		System.out.println("\nProcess No.\tProcess Size\tBlock no.");
// 	    for (int i = 0; i < b; i++)
// 	    {
// 	        System.out.print(" " + (i+1) + "\t\t" +
// 	                         processsize[i] + "\t\t");
// 	        if (allocation[i] != -1)
// 	            System.out.print(allocation[i] + 1);
// 	        else
// 	            System.out.print("Not Allocated");
// 	        System.out.println();
// 	    }   
		
// 	}
	

// }


import java.util.*;
class Firstfit 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of memory blocks: ");
        int numberOfMemoryBlocks = scanner.nextInt();
        int[] blockSize = new int[numberOfMemoryBlocks];
        for (int i = 0; i < numberOfMemoryBlocks; i++)
        {
            System.out.println("Enter the size of memory block " + (i + 1) + ": ");
            blockSize[i] = scanner.nextInt();
        }
        System.out.println("Enter the number of processes: ");
        int numberOfProcesses = scanner.nextInt();
        int[] processSize = new int[numberOfProcesses];
        for (int i = 0; i < numberOfProcesses; i++) 
        {
            System.out.println("Enter the size of process " + (i + 1) + ": ");
            processSize[i] = scanner.nextInt();
        }
        boolean[] isFree = new boolean[numberOfMemoryBlocks];
        Arrays.fill(isFree, true);
        for (int i = 0; i < processSize.length; i++) 
        {
            int firstFitIndex = -1;
            for (int j = 0; j < blockSize.length; j++) 
            {
                if (isFree[j] && blockSize[j] >= processSize[i]) 
                {
                    firstFitIndex = j;
                    break;
                }
            }
            if (firstFitIndex != -1) 
            {
                isFree[firstFitIndex] = false;
                System.out.println(" " + (i+1) + "\t\t" + processSize[i] + "\t\t" + (firstFitIndex+1));
            } else 
            {
                System.out.println("Process " + (i+1) + " cannot be allocated memory");
            }
        }
    }
}
