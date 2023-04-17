#include <iostream>
using namespace std;

int main(){
	
	int b, c = 10;
		
	cout<< "podaj wartosc b = " << endl;
	cin >> b;
	
	cout << "wykonujemy dzielenie a = b/c "<< endl;
	float a = static_cast<float>(b)/static_cast<float>(c);
	
	cout <<"wartosc ilorazu a = b/c = "	<< b/c << endl;
		
	
	
	return 0;
}