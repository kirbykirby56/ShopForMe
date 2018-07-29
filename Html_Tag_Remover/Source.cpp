#include<string>
#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main(int argc, char *argv[]) {
	fstream fr, fw;
	string file, working;
	vector<string> filecont;
	if (argc != 1) file = argv[1];
	else cin >> file;
	fr.open(file, ios::in);
	while (getline(fr, working)) {
		while (working.find("<b>") != string::npos) working.erase(working.find("<b>"), 3);
		while (working.find("</b>") != string::npos) working.erase(working.find("</b>"), 4);
		while (working.find("&amp;") != string::npos) working.erase(working.find("&amp;") + 1, 3);
		filecont.push_back(working);
	}
	fr.close();
	fw.open(file, ios::out);
	for (int i = 0; i < filecont.size(); i++) fw << filecont[i];
	fw.close();

	return 0;
}