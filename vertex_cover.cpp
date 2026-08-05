
#include <iostream>
#include <vector>
using namespace std;

class Graph{
    int V;
    vector<pair<int, int>> edges;
    
    public:
        Graph(int v){
            V=v;
        }
        
        void addEdge(int u, int v){
            edges.push_back({u, v});
        }
        
        void printGraph() {
            for (const auto &e : edges) {
                cout << "(" << e.first << ", " << e.second << ")\n";
            }
        }
        
        bool isVertexCover()
};

int main(){
    int n=8;
    Graph g(n);
    g.addEdge(1,6);
    g.addEdge(1,2);
    g.addEdge(1,4);
    g.addEdge(2,3);
    g.addEdge(2,4);
    g.addEdge(6,7);
    g.addEdge(4,7);
    g.addEdge(7,8);
    g.addEdge(3,5);
    g.addEdge(8,5);
    g.addEdge(3,8);
    
    g.printGraph();

    
    return 0;
}