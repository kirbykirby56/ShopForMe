#include<string>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main(int argc, char *argv[]){
	fstream fr, fw;
	string file, working;
	vector<string> filecont;
	if (argc != 1) file = argv[1];
	else cin >> file;
	fr.open(file, ios::in);
	while (getline(fr, working)) {
		bool b = true;
		for (int i = 0; i < filecont.size(); i++) if (filecont[i] == working) b = false;
		if(b)filecont.push_back(working);
	}
	fr.close();
	fw.open(file, ios::out);
	for (int i = 0; i < filecont.size(); i++) fw << filecont[i];
	fw.close();
	
	return 0;
}