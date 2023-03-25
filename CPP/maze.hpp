#include <iostream>
#include <list>

using namespace std;

#define cell_empty ' '
#define cell_blocked 'X'
#define cell_barrier_floor '='
#define cell_barrier_wall '|'
#define cell_start 'S'
#define cell_goal 'G'
#define cell_path '*'

typedef struct{
    int row;
    int column;
} MazeLocation;

class Maze{
    private:
        int rows = 10;
        int columns = 12;
        float sparseness = 0.2;
        MazeLocation start;
        MazeLocation goal;
        char grid[10][12];

    public:
        Maze();

        void create_maze();

        bool goal_test(MazeLocation ml);

        list<MazeLocation> successors(MazeLocation ml);

        void mark(list<MazeLocation> path);

        void clear(list<MazeLocation> path);

        void output();
};