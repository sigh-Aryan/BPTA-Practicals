#include <iostream>
#include <vector>
using namespace std;

class Graph {
    int V;
    vector<pair<int, int>> edges;

public:
    Graph(int v) {
        V = v;
    }

    void addEdge(int u, int v) {
        edges.push_back({u, v});
    }

    void printGraph() {
        cout << "\nEdges of the graph:\n";

        for (const auto &e : edges) {
            cout << "(" << e.first << ", " << e.second << ")\n";
        }
    }

    bool isVertexCover() {
        return false; // Add your vertex cover logic here
    }
};

int main() {
    int n, e;

    cout << "Enter number of vertices: ";
    cin >> n;

    Graph g(n);

    cout << "Enter number of edges: ";
    cin >> e;

    cout << "Enter the edges (u v):\n";

    for (int i = 0; i < e; i++) {
        int u, v;

        cout << "Edge " << i + 1 << ": ";
        cin >> u >> v;

        g.addEdge(u, v);
    }

    g.printGraph();

    return 0;
}
