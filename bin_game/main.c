#include "headers/bin_game.h"
#include <time.h>
#include <stdlib.h>
#include "headers/validator_module.h"
int main(const int const argc, const char * const argv[])
{
	const char * allow_flags[] = {
		"--help", 
		"-h"
	};
	int allowLen = sizeof allow_flags / sizeof allow_flags[0];
	void(*functions_for_args[])(void) = {
		help, 
		help
	};

	srand(time(NULL));
	if (argc > 1) {
		flagValidator(argc, argv, allow_flags, allowLen);
		flag_to_function_select(argc, argv, allow_flags, functions_for_args, allowLen);
	}
	else {
		//char mode[] = {'d','x','b'};
		//action(d);
		menu();
	}
	return 1;
}
