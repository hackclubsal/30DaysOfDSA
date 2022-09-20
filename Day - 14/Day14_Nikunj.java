// Q.13) Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
// Input: See the picture

// Output: 0 1 2 3 4

// Explanation:

// 0 is connected to 1 , 2 , 3.

// 2 is connected to 4.so starting from 0,

// it will go to 1 then 2 then 3.

// After this 2 to 4,

// thus bfs will be 0 1 2 3 4.

package Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {

	public static void main(String[] args) {
		Graph g = new Graph(5);
		g.addEdge(0, 1);
		g.addEdge(0, 2);
		g.addEdge(0, 3);
		g.addEdge(2, 4);

		System.out.println("-------Graph-------");
		g.printGraph();

		ArrayList<Integer> ans = bfsOfGraph(5, g.graph);
		System.out.println("\nBFS traversal :" + ans);
	}

	public static ArrayList<Integer> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {

		ArrayList<Integer> bfs = new ArrayList<>();
		boolean vis[] = new boolean[V];

		for (int i = 0; i < V; i++) {
			if (vis[i] == false) {
				Queue<Integer> q = new LinkedList<>();
				q.add(i);
				vis[i] = true;

				while (!q.isEmpty()) {
					Integer node = q.poll();
					bfs.add(node);
					for (Integer it : adj.get(node)) {
						if (vis[it] == false) {
							vis[it] = true;
							q.add(it);
						}
					}
				}
			}
		}

		return bfs;
	}

}


public class Graph {
		ArrayList<ArrayList<Integer>> graph;
		int v;
		
		Graph(int nodes){
			v=nodes;
			graph = new ArrayList<ArrayList<Integer>>();
			for(int i=0;i<v;i++) {
				graph.add(new ArrayList<Integer>());
			}
		}
		
		void addEdge(int v,int u) {
			graph.get(v).add(u);
			graph.get(u).add(v);
		}
		
		void printGraph() {
			for(int i=0;i<v;i++) {
				System.out.print ("Node "+i);
				for(int x:graph.get(i)) System.out.print(" -> "+x);
				System.out.println();
			}
			
		}
}

