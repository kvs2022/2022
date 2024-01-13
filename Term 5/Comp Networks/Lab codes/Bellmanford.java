import java.util.ArrayList;
import java.util.Arrays;

public
class Bellmanford{

private
    static void bellmanFord(int n, int m, int src, ArrayList<ArrayList<Integer>> edges){
    
        // create an array to store the path length from source to i
        int[] path = new int[n];

        // fill the array with the max value
        Arrays.fill(path, Integer.MAX_VALUE);

        // distance of source to source is 0
        path[src] = 0;

        int f = 1;

        // bellman ford algorithm
        for (int i = 0; i <= n; i++){
        
            for (int j = 0; j < m; j++){
            
                // u node
                int u = edges.get(j).get(0);
                
                // v node
                int v = edges.get(j).get(1);
                
                // edge weight
                int w = edges.get(j).get(2);

                if (i == n && path[u]!= Integer.MAX_VALUE && path[v] > (path[u] + w) ){
                
                    System.out.println("There is a negative cycle in the graph");
                    f = 0;
                    break;
                }
                // relaxation
                else if (i<n && path[u] != Integer.MAX_VALUE && path[v] > (path[u] + w)){
                
                    path[v] = path[u] + w;
                }
            }
        }

        // if there is no negative cyle
        if (f == 1){
        
            // then print the shortest path of every node from the source node
            for (int i = 0; i < n; i++){
            
                System.out.print("The shortest path between " + src + " and " + i + " is: ");
                
                if(path[i]==Integer.MAX_VALUE){
					System.out.println("No Path");
            	}
            	else{
                	System.out.println(path[i]); 
            	} 
            }
        }
    }

    // driver code
public static void main(String[] args){
    
        int n = 5, m = 7, src = 0;
        ArrayList<ArrayList<Integer>> edges = new ArrayList<ArrayList<Integer>>();

        ArrayList<Integer> edge1 = new ArrayList<Integer>();
        edge1.add(2);
        edge1.add(4);
        edge1.add(3);

        ArrayList<Integer> edge2 = new ArrayList<Integer>();
        edge2.add(4);
        edge2.add(3);
        edge2.add(3);

        ArrayList<Integer> edge3 = new ArrayList<Integer>();
        edge3.add(0);
        edge3.add(2);
        edge3.add(2);

        ArrayList<Integer> edge4 = new ArrayList<Integer>();
        edge4.add(3);
        edge4.add(1);
        edge4.add(-3);

        ArrayList<Integer> edge5 = new ArrayList<Integer>();
        edge5.add(1);
        edge5.add(2);
        edge5.add(1);

        ArrayList<Integer> edge6 = new ArrayList<Integer>();
        edge6.add(2);
        edge6.add(3);
        edge6.add(4);

        ArrayList<Integer> edge7 = new ArrayList<Integer>();
        edge7.add(0);
        edge7.add(1);
        edge7.add(-1);

        edges.add(edge1);
        edges.add(edge2);
        edges.add(edge3);
        edges.add(edge4);
        edges.add(edge5);
        edges.add(edge6);
        edges.add(edge7);

        bellmanFord(n, m, src, edges);
    }
}
