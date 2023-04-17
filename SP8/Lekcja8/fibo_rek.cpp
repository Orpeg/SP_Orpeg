#include <iostream>

unsigned long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    std::cout << "Podaj liczbe calkowita n: ";
    std::cin >> n;

    if (n < 0) {
        std::cout << "Nieprawidlowa wartosc n. Podaj liczbe nieujemna." << std::endl;
    } else {
        unsigned long long wynik = fibonacci(n);
        std::cout << "Liczba Fibonacciego dla n = " << n << ": " << wynik << std::endl;
    }

    return 0;
}
