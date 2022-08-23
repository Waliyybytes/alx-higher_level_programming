#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - if a singly list is a cycle
 * @list: list to check
 * Return: 1 for SUCCESS
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
