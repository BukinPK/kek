#include "headers/bin_game.h"

mod_t bd = {
	.index = 0,
	.in = 2,
	.out = 10,
	.min_rand = 0b0000,
	.max_rand = 0b1111,
	.prompt = "Переведите в DEC: %-*i ",
	.err = " \e[31;1m%2s\e[0m %d\n"
};


mod_t db = {
	.index = 2,
	.in = 10,
	.out = 2,
	.min_rand = 0,
	.max_rand = 31,
	.prompt = "Переведите в BIN: %-*i ",
	.err = " \e[31;1m%2s\e[0m %i\n"
};

mod_t xd = {
	.index = 0,
	.in = 16,
	.out = 10,
	.min_rand = 10,
	.max_rand = 15,
	.prompt = "Переведите в DEC: 0x%-*X ",
	.err = " \e[31;1m%2s\e[0m %d\n"
};

mod_t dx = {
	.index = 1,
	.in = 10,
	.out = 16,
	.min_rand = 10,
	.max_rand = 15,
	.prompt = "Переведите в HEX: %-*i ",
	.err = " \e[31;1m%2s\e[0m %X\n"
};

mod_t bx = {
	.index = 1,
	.in = 2,
	.out = 16,
	.min_rand = 0xA,
	.max_rand = 0xF,
	.prompt = "Переведите в HEX: 0b%-*i ",
	.err = " \e[31;1m%2s\e[0m %X\n"
};

mod_t xb = {
	.index = 2,
	.in = 16,
	.out = 2,
	.min_rand = 0xA,
	.max_rand = 0xF,
	.prompt = "Переведите в BIN: 0x%-0*X ",
	.err = " \e[31;1m%2s\e[0m %i\n"
};

//temp
mod_t cs = { };
