#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <string.h>
using namespace std;


vector<string> split(string phrase){
    vector<string> list;
    char *pch = strtok (phrase," ,.-");
  	while (pch != NULL)
  	{
    	list.push_back(string(pch));
    	pch = strtok (NULL, " ,.-");
  	}
    return list;
}


int main(int argc, char **argv){
	std::string::size_type sz;     // alias of size_t
	ifstream file(argv[1]);
	ofstream out(argv[2]);
	string line;
	while(getline(file,line)){
		vector<string> lines = split(line);
		for (std::vector<string>::iterator i = lines.begin(); i != lines.end(); ++i)
		{
			if(*i == "vertex"){
				out<<stof(lines[5],&sz)/1000<<" "<<stof(lines[6],&sz)/1000<<" "<<stof(lines[5],&sz)/1000<<endl;
				break;
			}
		}
	}
	out.close();
	file.close();
}
