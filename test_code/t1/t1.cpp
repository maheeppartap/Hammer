
#include <iostream>
#include <cstdlib>

int foo(int a, int b, int c)
{
    if (c > 10){
        return a + b + c; 
    }
    else{
        return std::abs(a - b);
    }
}

int main(int argc, char* argv[]) {
    if (argc != 4) { // argc should be 4 because it includes the program name
        std::cerr << "Provide 3 integer arguments\n";
        exit(EXIT_FAILURE);
    }

    auto ret = foo(std::atoi(argv[1]), std::atoi(argv[2]), std::atoi(argv[3]));

    // Example usage of ret
    std::cout << "Result: " << ret << std::endl;

    return ret;
}