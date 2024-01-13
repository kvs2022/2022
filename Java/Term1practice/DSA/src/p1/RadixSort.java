package p1;

import java.util.Arrays;

public class RadixSort {

  public static void sort(int[] arr) {
    int max = getMax(arr);

    for (int place = 1; max / place > 0; place *= 10) {
      countSort(arr, place);
    }
  }

  private static void countSort(int[] arr, int place) {
    int[] output = new int[arr.length];
    int[] count = new int[10];

    for (int i = 0; i < arr.length; i++) {
      int digit = (arr[i] / place) % 10;
      count[digit]++;
    }

    for (int i = 1; i < count.length; i++) {
      count[i] += count[i - 1];
    }

    for (int i = arr.length - 1; i >= 0; i--) {
      int digit = (arr[i] / place) % 10;
      output[count[digit] - 1] = arr[i];
      count[digit]--;
    }

    for (int i = 0; i < arr.length; i++) {
      arr[i] = output[i];
    }
  }

  private static int getMax(int[] arr) {
    int max = arr[0];

    for (int i = 1; i < arr.length; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
    }

    return max;
  }

  public static void main(String[] args) {
    int[] arr = {170, 45, 75, 90, 802, 24, 2, 66};
    sort(arr);
    System.out.println(Arrays.toString(arr));
  }
}
