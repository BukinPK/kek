#include "headers/validator_module.h"

void flagValidator (
		const int const argc, 
		const char * const argv[], 
		const char * allow_flags[], 
		int allow_length )
{
	for (int i = 1; i < argc; i++) {
		for (int j = 0; j < allow_length; j++) {
			if (strcmp(argv[i], allow_flags[j]) == 0)
				break;
			if (j == allow_length -1) {
				printf("ERROR \e[31m%s\e[0m нахуй иди с такими аргументами.\n", argv[i]);
				exit(1);
			}
		}
	}
}

void flag_to_function_select (
		const int argc, 
		const char * const argv[], 
		const char * allow_flags[], 
		void(*functions_for_args[])(void), 
		int allow_length )
{
	for (int i = 1; i < argc; i++) {
		for (int j = 0; j < allow_length; j++) {
			if (strcmp(argv[i], allow_flags[j]) == 0) {
				functions_for_args[j]();
				break;
			}
		}
	}
}
