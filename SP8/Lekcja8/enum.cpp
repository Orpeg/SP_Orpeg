#include <iostream>

enum DzienTygodnia {
    Poniedzialek = 1,
    Wtorek,
    Sroda,
    Czwartek,
    Piatek,
    Sobota,
    Niedziela
};

int main() {
    int numer;
    std::cout << "Podaj numer dnia tygodnia (1-7): ";
    std::cin >> numer;

    DzienTygodnia dzien = static_cast<DzienTygodnia>(numer);

    switch (dzien) {
        case Poniedzialek:
            std::cout << "Poniedzialek";
            break;
        case Wtorek:
            std::cout << "Wtorek";
            break;
        case Sroda:
            std::cout << "Sroda";
            break;
        case Czwartek:
            std::cout << "Czwartek";
            break;
        case Piatek:
            std::cout << "Piatek";
            break;
        case Sobota:
            std::cout << "Sobota";
            break;
        case Niedziela:
            std::cout << "Niedziela";
            break;
        default:
            std::cout << "Nieprawidlowy numer dnia tygodnia.";
    }

    return 0;
}
