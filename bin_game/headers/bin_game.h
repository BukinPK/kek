typedef struct mod {
	char in;
	char out;
	int min_rand;
	int max_rand;
	char index;
	char *prompt;
	int ran;
	char *err;
} mod_t;
mod_t bd, db, xd, dx, cs, bx, xb;
//modes
void help(void);
char menu(void); 
void action(mod_t mode);

//Принимает символы во внешний массив, в количестве count и диапазоне low - high
void char_to_array(char answer[], char count, char type);

// Считает количество символов в числе
char count_of_numbers(int num, char plus_zero_number);

// Принимают массив символов числового диапазона и преобразует в int
int int_chars_converter(char answer[], char count);
int hex_chars_converter(char answer[], char count);
int bin_chars_converter(char answer[], char count);

int dec_bin_converter(int num);
int ran_format_in(mod_t mode);
int ran_format_out(mod_t mode);
