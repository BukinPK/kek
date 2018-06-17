#include "headers/conio.h"
#include "headers/bin_game.h"
#include <stdio.h>


void char_to_array(char answer[], char count, char type)
{
	for (char i=0; i < count;){
		answer[i] = getch();
		switch (type) {
			case 16:
				if (answer[i] > 0x2F && answer[i] < 0x3A) { 
						printf("%c",answer[i]);
						i++;
					}
				else if (answer[i] > 0x60 && answer[i] < 0x67) {
					printf("%c",answer[i]-0x20);
					i++;
				}
				else if (answer[i] == 0x7F && i > 0) {
					putchar('\b');
					putchar(' ');
					putchar('\b');
					i--;
				}
				else if (answer[i] == 'q') {
					answer[0] = 'q';
					return;
				}
			break;
			case 10:
				if (answer[i] > 0x2F && answer[i] < 0x3A) { 
					printf("%c",answer[i]);
					i++;
				}
				else if (answer[i] == 0x7F && i > 0) {
					putchar('\b');
					putchar(' ');
					putchar('\b');
					i--;
				}
				else if (answer[i] == 'q') {
					answer[0] = 'q';
					return;
				}
			break;
			case 2:
				if (answer[i] > 0x2F && answer[i] < 0x32) {
					printf("%c",answer[i]);
					i++;
				}
				else if (answer[i] == 0x7F && i > 0) {
					putchar('\b');
					putchar(' ');
					putchar('\b');
					i--;
				}
				else if (answer[i] == 'q') {
					answer[0] = 'q';
					return;
				}
		}
	}
}

int hex_chars_converter(char answer[], char count) 
{
	unsigned int zeros = 1;
	for (char i=1; i < count; i++)
		zeros = (zeros*16);
	int result = 0;
	for (char i=0; i < count; i++) {
		if (answer[i] < 0x3A)
			result += (answer[i] - 0x30) * zeros;
		else
			result += (answer[i] - 0x57) * zeros;
		zeros /= 16;
	}
	return result;
}

int int_chars_converter(char answer[], char count) 
{
	unsigned int zeros = 1;
	for (char i=1; i < count; i++)
		zeros = (zeros*10);
	int result = 0;
	for (char i=0; i < count; i++) {
		result += (answer[i] - 48) * zeros;
		zeros /= 10;
	}
	return result;
}

int bin_chars_converter(char answer[], char count)
{
	unsigned int zeros = 1;
	for (char i=1; i < count; i++)
		zeros = (zeros*2);
	int result = 0;
	for (char i=0; i < count; i++) {
		result += (answer[i] - 48) * zeros;
		zeros /= 2;
	}
	return result;
}

int dec_bin_converter (int num)
{
	int pos = 1;
	int res = 0;
	while (num > 0) {
		res += (num % 2)*pos;
		pos *= 10;
		num /= 2;
	}
	return res;
}
int ran_format_in(mod_t mode) {
	if (mode.in != 2) return mode.ran;
	else return dec_bin_converter(mode.ran);
}
int ran_format_out(mod_t mode) {
	if (mode.out != 2) return mode.ran;
	else return dec_bin_converter(mode.ran);
}

char count_of_numbers(int num, char plus_zero_number) 
{
	char max = plus_zero_number-1;
	char count_of_numbers = 1;
	for (int x = num; x > max; x /= plus_zero_number)
		count_of_numbers++;
	return count_of_numbers;
}

