#include "maze.hpp"

using namespace std;

Maze::Maze(){
    this->start.row = 0;
    this->start.column = 1;

    this->goal.row = 9;
    this->goal.column = 10;

    this->create_maze();
}

void Maze::create_maze(){
    for(int i = 0; i < this->rows; i++){
        for(int j = 0; j < this->columns; j++){
            this->grid[i][j] = cell_empty;
        }
    }

    for(int i = 0; i < this->rows; i++){
        this->grid[i][0] = cell_barrier_wall;
        this->grid[i][this->columns-1] = cell_barrier_wall;
    }

    for(int i = 0; i < this->columns; i++){
        this->grid[0][i] = cell_barrier_floor;
        this->grid[this->rows-1][i] = cell_barrier_floor;
    }

    this->grid[this->start.row][this->start.column] = cell_start;
    this->grid[this->goal.row][this->goal.column] = cell_goal;

    this->grid[1][4] = cell_blocked;
    this->grid[1][5] = cell_blocked;
    this->grid[2][2] = cell_blocked;
    this->grid[2][7] = cell_blocked;
    this->grid[2][8] = cell_blocked;
    this->grid[2][10] = cell_blocked;
    this->grid[3][1] = cell_blocked;
    this->grid[3][3] = cell_blocked;
    this->grid[3][4] = cell_blocked;
    this->grid[3][5] = cell_blocked;
    this->grid[4][5] = cell_blocked;
    this->grid[4][6] = cell_blocked;
    this->grid[4][8] = cell_blocked;
    this->grid[4][9] = cell_blocked;
    this->grid[5][2] = cell_blocked;
    this->grid[5][9] = cell_blocked;
    this->grid[6][3] = cell_blocked;
    this->grid[6][6] = cell_blocked;
    this->grid[6][7] = cell_blocked;
    this->grid[6][8] = cell_blocked;
    this->grid[6][9] = cell_blocked;
    this->grid[6][10] = cell_blocked;
    this->grid[7][3] = cell_blocked;
    this->grid[7][5] = cell_blocked;
    this->grid[7][10] = cell_blocked;
    this->grid[8][2] = cell_blocked;
    this->grid[8][7] = cell_blocked;
}

bool Maze::goal_test(MazeLocation ml){
    if (ml.row == this->goal.row){
        if(ml.column == this->goal.column){
            return true;
        } else {
            return false;
        }
    } else {
        return false;
    }
}

list<MazeLocation> Maze::successors(MazeLocation ml){
    list<MazeLocation> locations;
    MazeLocation aux;

    if((ml.row+1 < this->rows && this->grid[ml.row+1][ml.column] != cell_blocked) &&
       (ml.row+1 < this->rows && this->grid[ml.row+1][ml.column] != cell_barrier_floor) &&
       (ml.row+1 < this->rows && this->grid[ml.row+1][ml.column] != cell_barrier_wall)){
       aux.row = ml.row+1;
       aux.column = ml.column;
       
       locations.push_back(aux);
    }

    if((ml.row-1 >= 0 && this->grid[ml.row-1][ml.column] != cell_blocked) &&
       (ml.row-1 >= 0 && this->grid[ml.row-1][ml.column] != cell_barrier_floor) &&
       (ml.row-1 >= 0 && this->grid[ml.row-1][ml.column] != cell_barrier_wall)){
        aux.row = ml.row-1;
        aux.column = ml.column;

        locations.push_back(aux);
    }

    if((ml.row+1 < this->columns && this->grid[ml.row][ml.column+1] != cell_blocked) &&
       (ml.row+1 < this->columns && this->grid[ml.row][ml.column+1] != cell_barrier_floor) &&
       (ml.row+1 < this->columns && this->grid[ml.row][ml.column+1] != cell_barrier_wall)){
        aux.row = ml.row;
        aux.column = ml.column+1;

        locations.push_back(aux);
    }

    if((ml.row-1 >= 0 && this->grid[ml.row][ml.column-1] != cell_blocked) &&
       (ml.row-1 >= 0 && this->grid[ml.row][ml.column-1] != cell_barrier_floor) &&
       (ml.row-1 >= 0 && this->grid[ml.row][ml.column-1] != cell_barrier_wall)){
        aux.row = ml.row;
        aux.column = ml.column-1;

        locations.push_back(aux);
    }

    return locations;
}

void Maze::mark(list<MazeLocation> path){
    list<MazeLocation>::iterator it;

    for(it = path.begin(); it != path.end(); ++it){
        this->grid[it->row][it->column] = cell_path;
    }

    this->grid[this->start.row][this->start.column] = cell_start;
    this->grid[this->goal.row][this->goal.column] = cell_goal;
}

void Maze::clear(list<MazeLocation> path){
    list<MazeLocation>::iterator it;

    for(it = path.begin(); it != path.end(); ++it){
        this->grid[it->row][it->column] = cell_empty;
    }

    this->grid[this->start.row][this->start.column] = cell_start;
    this->grid[this->goal.row][this->goal.column] = cell_goal;
}

void Maze::output(){
    for(int i = 0; i < this->rows; i++){
        for(int j = 0; j < this->columns; j++){
            cout << this->grid[i][j];
        }
        cout << '\n';
    }
}