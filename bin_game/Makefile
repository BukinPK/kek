NAME=main
CFLAGS +=-g
.PHONY: all clean install uninstall bin_game $(NAME)

all: $(NAME)

install:
	sudo install $(NAME) /bin/bin_game
uninstall:
	sudo rm -f /bin/bin_game
clean:
	rm -f $(NAME)
$(NAME): 
	gcc -o $(NAME) *.c $(CFLAGS)

