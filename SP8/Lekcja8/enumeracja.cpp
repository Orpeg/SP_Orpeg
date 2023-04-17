#include <iostream>
using namespace std;

int main() {

    enum dzien {
        PONIEDZIALEK = 1, WTOREK = 2, SRODA = 3, CZWARTEK = 4, PIATEK = 5, SOBOTA = 6, NIEDZIELA = 7
    };

    dzien d = WTOREK;

    cout << "Wybrany dzien: " << d << endl;

    return 0;
}
