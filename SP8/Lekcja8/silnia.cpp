#include <iostream>
using namespace std;

int main() {

    unsigned long long int n, silnia = 1;
    cout << "podaj liczbe calkowita do policzenia silni  " << endl;
    cin >> n;

    if (n > 20) {
        cout << "Uwaga: Przy liczbie wiekszej niz 20, wynik moze byc niepoprawny z powodu przekroczenia zakresu." << endl;
    }

    for (int i = 1; i <= n; i++) {

        silnia *= i;

    }

    cout << "silnia " << n << "! wynosi  " << silnia << endl;

    return 0;
}
