#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void flagValidator (
			const int const argc, 
			const char * const argv[], 
			const char * allow_flags[], 
			int allowLen
);
void flag_to_function_select (
			const int argc, 
			const char * const argv[], 
			const char * allow_flags[], 
			void(*functions_for_args[])(void), 
			int allowLen
);
