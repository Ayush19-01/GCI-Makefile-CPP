#include <iostream>
#include <fstream>
using namespace std;
int main () {
  ofstream file;
  file.open ("read.txt");
  file << "1 4 9 16 25 36 49 64 81 100";
  file.close();
  return 0;
}