CC = gcc
CFLAGS = -Wall -Wextra -Werror
NAME = delete_dnodeint
SRC = main.c free_dlistint.c print_dlistint.c add_dnodeint_end.c \
			delete_dnodeint_at_index.c
OBJ = $(SRC:.c=.o)

.PHONY: all clean fclean re

all: lists.h $(OBJ)
	$(CC) -o $(NAME) $(OBJ)

clean:
	$(RM) $(NAME)

oclean:
	$(RM) *~ $(OBJ)

fclean: clean oclean

re: fclean all
