#include "headers/conio.h"
#include <stdlib.h>
#include <stdio.h>
#include "headers/bin_game.h"

char menu(void) {
	char *main_menu[] = {"Bin to Dec", "Dec to Bin", "Hex to Dec", 
		"Dec to Hex", "Bin to Hex", "Hex to Bin", "Custom"
	};
	mod_t mode[] = {bd, db, xd, dx, bx, xb, cs};
	char menu_len = sizeof main_menu / sizeof main_menu[0];
	while (1) {
		printf("\n\nВыберите режим:\n");	
		for (int i = 0; i < menu_len; i++) {
			printf("%d: %s\n", i+1, main_menu[i]);	
		}
		while (1) {
			char x = getch();
			if ( x > 0x30 && x < 0x30 + menu_len + 1 ) {
				x -= 0x31;
				printf("Ваш выбор: %s\n", main_menu[x]);
				if (x == 6) 
					printf("Сорян, пока не пашет, выбери готовый.");
				else action(mode[x]);
				break;
			}
			else if (x == 'q') {
				printf("\nДо свидания.\n\n");
				exit(0);
			}
		}
	}
	return 0;
}

void action(mod_t mode) 
{
	char count_of_max_numbers = count_of_numbers(mode.max_rand, mode.in);
	char answer[count_of_max_numbers];
	int answer_result;
	char count_of_recive_numbers; 
	int(*converter[])(char answer[], char count) = {
		int_chars_converter, hex_chars_converter, bin_chars_converter
	};
	while(1){
		mode.ran = mode.min_rand + rand() % (mode.max_rand + 1 - mode.min_rand);
		printf(mode.prompt, count_of_max_numbers, ran_format_in(mode));
		count_of_recive_numbers = count_of_numbers(mode.ran, mode.out);

		char_to_array(answer, count_of_recive_numbers, mode.out);
		if (answer[0] == 'q') return;
		answer_result = converter[mode.index](answer, count_of_recive_numbers);
		if (answer_result == mode.ran) {	
			printf(" \e[32;1m%2s\e[0m\n", "WIN");
		}
		else {
			if ((answer_result >= mode.min_rand) && (answer_result <= mode.max_rand))
				printf(mode.err, "ERROR", ran_format_out(mode));
			else printf(" \e[41;37m%2s\e[0m\n", " Incorrect number ");
		}
	}
}

void help(void){
	printf("No one help you.\n"); 
}
