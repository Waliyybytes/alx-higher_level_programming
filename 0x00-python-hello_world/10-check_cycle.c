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
	listint_t *other;

	current = list;
	other = list;
	while (current != NULL && other !=NULL && other->next != NULL)
	{
		current = current->next;
		other = other->next->next;
		if (current == other)
			return (1);
	}
	return (0);
}
