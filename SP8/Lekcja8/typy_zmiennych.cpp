#include <iostream>

int main() {
    int a, b, c;
    std::cout << "Podaj trzy liczby calkowite: ";
    std::cin >> a >> b >> c;
    
    int suma = a + b + c;
    int roznica = a - b - c;
    int iloczyn = a * b * c;
    double iloraz = static_cast<double>(a) / b / c;

    std::cout << "Suma: " << suma << std::endl;
    std::cout << "Roznica: " << roznica << std::endl;
    std::cout << "Iloczyn: " << iloczyn << std::endl;
    std::cout << "Iloraz: " << iloraz << std::endl;

    return 0;
}
